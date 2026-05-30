"""Tests for mp_adapter: Materials Project property extraction."""

import json
import pytest
from unittest.mock import MagicMock, patch
from dataclasses import dataclass

# Import module under test
import sys
sys.path.insert(0, ".")
from scripts.mp_adapter import (
    SYSTEM_TO_CHEMSYS,
    CRYSTAL_SYSTEM_TO_PHASE,
    _determine_phase,
    _pick_best_material,
    _extract_elastic_props,
    _extract_lattice_constant,
    _extract_thermo_props,
    MpProperty,
    MpExtractionResult,
    extract_all,
)


# ---------------------------------------------------------------------------
# Helpers: mock MP documents
# ---------------------------------------------------------------------------


def make_mock_doc(
    mp_id="mp-149",
    formula="Si",
    crystal_system="cubic",
    sg_number=229,
    a=3.165,
    c11=160.0,
    c12=64.0,
    c44=78.0,
    k_vrh=96.0,
    formation_energy=-0.5,
    energy_above_hull=0.0,
    has_elastic=True,
):
    """Create a mock MP summary document."""
    doc = MagicMock()
    doc.material_id = mp_id
    doc.formula_pretty = formula
    doc.energy_above_hull = energy_above_hull

    # Symmetry
    sym = MagicMock()
    sym.crystal_system = crystal_system
    sym.number = sg_number
    doc.symmetry = sym

    # Structure
    lattice = MagicMock()
    lattice.a = a
    structure = MagicMock()
    structure.lattice = lattice
    doc.structure = structure

    # Elasticity
    if has_elastic:
        elast = MagicMock()
        elast.k_vrh = k_vrh
        elast.elastic_tensor = [
            [c11, c12, c12, 0, 0, 0],
            [c12, c11, c12, 0, 0, 0],
            [c12, c12, c11, 0, 0, 0],
            [0, 0, 0, c44, 0, 0],
            [0, 0, 0, 0, c44, 0],
            [0, 0, 0, 0, 0, c44],
        ]
        doc.elasticity = elast
    else:
        doc.elasticity = None

    # Thermo
    doc.formation_energy_per_atom = formation_energy

    return doc


# ---------------------------------------------------------------------------
# Tests: SYSTEM_TO_CHEMSYS mapping
# ---------------------------------------------------------------------------


class TestChemsysMapping:
    def test_all_target_systems_have_mapping(self):
        """Every gap_analyzer target system should have a chemsys mapping."""
        from scripts.gap_analyzer import TARGET_SYSTEMS
        for ts in TARGET_SYSTEMS:
            es = ts["element_system"]
            assert es in SYSTEM_TO_CHEMSYS, f"Missing chemsys mapping for {es}"

    def test_pure_elements(self):
        assert SYSTEM_TO_CHEMSYS["U"] == "U"
        assert SYSTEM_TO_CHEMSYS["Mo"] == "Mo"
        assert SYSTEM_TO_CHEMSYS["Zr"] == "Zr"

    def test_alloys(self):
        assert SYSTEM_TO_CHEMSYS["U-Mo"] == "U-Mo"
        assert SYSTEM_TO_CHEMSYS["U-Zr"] == "U-Zr"
        assert SYSTEM_TO_CHEMSYS["U-Pu-Zr"] == "U-Pu-Zr"

    def test_compound(self):
        assert SYSTEM_TO_CHEMSYS["SiC"] == "Si-C"


# ---------------------------------------------------------------------------
# Tests: phase determination
# ---------------------------------------------------------------------------


class TestPhaseDetermination:
    def test_bcc_spacegroup(self):
        doc = make_mock_doc(sg_number=229)  # Im-3m
        assert _determine_phase(doc) == "BCC"

    def test_hcp_spacegroup(self):
        doc = make_mock_doc(crystal_system="hexagonal", sg_number=194)  # P6_3/mmc
        assert _determine_phase(doc) == "HCP"

    def test_fallback_to_crystal_system(self):
        doc = make_mock_doc(crystal_system="tetragonal", sg_number=99)
        assert _determine_phase(doc) == "BCT"

    def test_no_symmetry(self):
        doc = MagicMock()
        doc.symmetry = None
        assert _determine_phase(doc) == "unknown"


# ---------------------------------------------------------------------------
# Tests: property extraction
# ---------------------------------------------------------------------------


class TestExtractElasticProps:
    def test_cubic_elastic_constants(self):
        doc = make_mock_doc(c11=160, c12=64, c44=78, k_vrh=96)
        props = _extract_elastic_props(doc, "U", "BCC")
        prop_names = [p.property for p in props]
        assert "C11" in prop_names
        assert "C12" in prop_names
        assert "C44" in prop_names
        assert "bulk_modulus" in prop_names
        # Check values
        c11 = next(p for p in props if p.property == "C11")
        assert c11.value == 160.0
        assert c11.unit == "GPa"
        assert c11.method == "DFT"
        assert c11.confidence == "medium"

    def test_no_elasticity(self):
        doc = make_mock_doc(has_elastic=False)
        props = _extract_elastic_props(doc, "U", "BCC")
        assert len(props) == 0

    def test_bulk_modulus_positive(self):
        doc = make_mock_doc(k_vrh=96)
        props = _extract_elastic_props(doc, "Mo", "BCC")
        bm = next(p for p in props if p.property == "bulk_modulus")
        assert bm.value == 96.0


class TestExtractLatticeConstant:
    def test_valid_lattice(self):
        doc = make_mock_doc(a=3.165)
        props = _extract_lattice_constant(doc, "U", "BCC")
        assert len(props) == 1
        assert props[0].property == "lattice_constant"
        assert props[0].value == 3.165
        assert props[0].unit == "Å"

    def test_out_of_range(self):
        doc = make_mock_doc(a=0.5)  # too small
        props = _extract_lattice_constant(doc, "U", "BCC")
        assert len(props) == 0

    def test_no_structure(self):
        doc = MagicMock()
        doc.structure = None
        props = _extract_lattice_constant(doc, "U", "BCC")
        assert len(props) == 0


class TestExtractThermoProps:
    def test_formation_energy(self):
        doc = make_mock_doc(formation_energy=-0.5)
        props = _extract_thermo_props(doc, "U", "BCC")
        assert len(props) == 1
        assert props[0].property == "formation_energy"
        assert props[0].value == -0.5

    def test_none_formation_energy(self):
        doc = make_mock_doc()
        doc.formation_energy_per_atom = None
        props = _extract_thermo_props(doc, "U", "BCC")
        assert len(props) == 0


# ---------------------------------------------------------------------------
# Tests: material selection
# ---------------------------------------------------------------------------


class TestPickBestMaterial:
    def test_prefers_on_hull(self):
        """When multiple docs share the same phase, pick the one on the hull."""
        on_hull = make_mock_doc(energy_above_hull=0.0)
        off_hull = make_mock_doc(energy_above_hull=0.5, mp_id="mp-999")
        result = _pick_best_material([off_hull, on_hull], "U", "BCC")
        # Only one BCC doc returned (dedup by phase), should be the on_hull one
        assert len(result) == 1
        assert str(result[0].material_id) == "mp-149"

    def test_prefers_matching_phase(self):
        bcc = make_mock_doc(crystal_system="cubic", sg_number=229)
        hcp = make_mock_doc(crystal_system="hexagonal", sg_number=194, mp_id="mp-999")
        result = _pick_best_material([hcp, bcc], "U", "BCC")
        assert str(result[0].material_id) == "mp-149"

    def test_prefers_with_elasticity(self):
        no_elastic = make_mock_doc(has_elastic=False, mp_id="mp-111")
        with_elastic = make_mock_doc(has_elastic=True, mp_id="mp-222")
        result = _pick_best_material([no_elastic, with_elastic], "U", "BCC")
        assert str(result[0].material_id) == "mp-222"

    def test_empty_input(self):
        result = _pick_best_material([], "U", "BCC")
        assert result == []

    def test_max_3_phases(self):
        docs = [
            make_mock_doc(crystal_system="cubic", sg_number=229, mp_id=f"mp-{i}")
            for i in range(5)
        ]
        result = _pick_best_material(docs, "U", "BCC")
        assert len(result) <= 3


# ---------------------------------------------------------------------------
# Tests: dry run
# ---------------------------------------------------------------------------


class TestDryRun:
    def test_dry_run_no_api_key_needed(self):
        result = extract_all(dry_run=True)
        assert result.total_queried > 0
        assert result.total_properties == 0  # no actual extraction
        assert len(result.errors) == 0  # dry run should not error on missing key

    def test_dry_run_with_systems_filter(self):
        result = extract_all(dry_run=True, systems=["U", "Mo"])
        assert result.total_queried == 2
        assert len(result.errors) == 0


# ---------------------------------------------------------------------------
# Tests: integration with write_ref_value pipeline
# ---------------------------------------------------------------------------


class TestPipelineIntegration:
    def test_extracted_props_pass_quality_gate(self):
        """Extracted properties should pass write_ref_value quality gate."""
        from scripts.write_ref_value import passes_quality_gate

        doc = make_mock_doc(c11=160, c12=64, c44=78, k_vrh=96, a=3.165)
        props = _extract_elastic_props(doc, "U", "BCC")
        props.extend(_extract_lattice_constant(doc, "U", "BCC"))

        for p in props:
            ref = {
                "element_system": p.element_system,
                "phase": p.phase,
                "property": p.property,
                "value": p.value,
                "unit": p.unit,
                "method": p.method,
                "source": p.source,
                "confidence": p.confidence,
            }
            assert passes_quality_gate(ref), f"Quality gate failed for {p.property}={p.value}"

    def test_extracted_props_pass_range_check(self):
        """Values should be within property-mapping.json ranges."""
        from scripts.write_ref_value import passes_range_check

        doc = make_mock_doc(c11=160, c12=64, c44=78, k_vrh=96)
        props = _extract_elastic_props(doc, "Mo", "BCC")

        for p in props:
            assert passes_range_check(p.property, p.value), \
                f"Range check failed for {p.property}={p.value}"


# ---------------------------------------------------------------------------
# Tests: MpProperty serialization
# ---------------------------------------------------------------------------


class TestSerialization:
    def test_to_dict_roundtrip(self):
        p = MpProperty(
            element_system="U", phase="BCC",
            property="C11", value=160.0, unit="GPa",
            method="DFT", source="Materials Project (mp-149)",
            confidence="medium", mp_id="mp-149",
            chemsys="U", crystal_system="cubic", spacegroup_number=229,
        )
        d = p.__dict__ if hasattr(p, '__dict__') else {}
        # MpProperty is a dataclass
        from dataclasses import asdict
        d = asdict(p)
        json_str = json.dumps(d)
        parsed = json.loads(json_str)
        assert parsed["element_system"] == "U"
        assert parsed["value"] == 160.0
        assert parsed["confidence"] == "medium"
