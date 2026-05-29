"""End-to-end test: U-Mo BCC reference value gap fill pipeline."""
import json
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from gap_analyzer import load_target_systems, compute_gaps, load_existing_refs
from cache_query import cache_query, CacheLevel
from adapter_nfmd import adapt_nfmd_param
from adapter_wiki import adapt_wiki_param
from adapter_ontology import adapt_ontology_individual
from write_ref_value import write_ref_value, WriteStatus


class TestE2EUmoBCC:
    """Test the complete pipeline for U-Mo BCC system."""

    def test_phase1_gap_analysis_identifies_umo_gaps(self):
        """Phase 1: Gap analysis should find U-Mo BCC gaps."""
        targets = load_target_systems()
        # Simulate existing refs that DON'T include U-Mo elastic constants
        existing = load_existing_refs([
            {"element_system": "U-Mo", "phase": "BCC", "property": "lattice_constant"},
            {"element_system": "U", "phase": "BCC", "property": "lattice_constant"},
        ])
        gaps = compute_gaps(targets, existing)

        # Should find U-Mo gaps for properties other than lattice_constant
        umo_gaps = [g for g in gaps if g.element_system == "U-Mo"]
        assert len(umo_gaps) > 0
        assert all(g.property != "lattice_constant" for g in umo_gaps)

    def test_phase2_cache_query_l2_hit_for_lattice_constant(self):
        """Phase 2: L2 cache should find U-Mo lattice constant."""
        mock_params = [
            {
                "material_raw": "U-Mo",
                "name": "lattice parameter",
                "symbol": "a",
                "value_scalar": 3.42,
                "unit": "Å",
                "temperature_k": 0,
                "method": "DFT (PBE)",
                "source_file": "hu-2016-jnm.md",
            }
        ]
        result = cache_query(
            "U-Mo", "BCC", "lattice_constant",
            _l1_rows=[],
            _l2_params=mock_params,
        )
        assert result is not None
        assert result.level == CacheLevel.L2
        assert abs(result.value - 3.42) < 0.01

    def test_phase2_nfmd_adapter_converts_correctly(self):
        """Phase 2: NFMD adapter should convert U-Mo C11 to ref_value format."""
        nfmd_param = {
            "material_raw": "U-Mo",
            "name": "elastic constant C11",
            "symbol": "C11",
            "value_scalar": 286.0,
            "unit": "GPa",
            "temperature_k": 0,
            "method": "DFT (PBE)",
            "source_file": "hu-2016-jnm.md",
        }
        adapted = adapt_nfmd_param(nfmd_param, phase="BCC")
        assert adapted["element_system"] == "U-Mo"
        assert adapted["property"] == "C11"
        assert adapted["value"] == 286.0
        assert adapted["confidence"] in ("high", "medium", "low")

    def test_phase2_wiki_adapter_converts_chinese(self):
        """Phase 2: Wiki adapter should convert Chinese U-Mo property."""
        wiki_param = {
            "system": "U-Mo",
            "phase": "BCC",
            "property_zh": "弹性常数 C11",
            "value": 286,
            "unit": "GPa",
            "temperature": "0K",
            "method": "DFT",
            "source": "Hu 2016, JNM",
        }
        adapted = adapt_wiki_param(wiki_param)
        assert adapted["property"] == "C11"
        assert adapted["element_system"] == "U-Mo"

    def test_phase3_write_high_confidence_auto(self):
        """Phase 3: Write high confidence U-Mo C11 auto."""
        ref = {
            "element_system": "U-Mo",
            "phase": "BCC",
            "property": "C11",
            "value": 286.0,
            "unit": "GPa",
            "method": "DFT (PBE)",
            "source": "Hu et al., 2016, JNM",
            "source_doi": "10.1016/j.jnucmat.2016.03.032",
            "confidence": "high",
            "uncertainty": None,
            "temperature": 0,
        }
        result = write_ref_value(ref, _existing=[])
        assert result.status == WriteStatus.WRITTEN_AUTO

    def test_phase3_write_medium_needs_review(self):
        """Phase 3: Write medium confidence needs review."""
        ref = {
            "element_system": "U-Mo",
            "phase": "BCC",
            "property": "C44",
            "value": 73.0,
            "unit": "GPa",
            "method": "DFT",
            "source": "Unknown paper",
            "source_doi": None,
            "confidence": "medium",
            "uncertainty": None,
            "temperature": 0,
        }
        result = write_ref_value(ref, _existing=[])
        assert result.status == WriteStatus.WRITTEN_PENDING_REVIEW

    def test_phase3_duplicate_rejected(self):
        """Phase 3: Duplicate U-Mo lattice_constant rejected."""
        existing = [
            {"element_system": "U-Mo", "phase": "BCC", "property": "lattice_constant",
             "method": "DFT (PBE)", "source": "Hu et al., 2016, JNM"},
        ]
        ref = {
            "element_system": "U-Mo", "phase": "BCC", "property": "lattice_constant",
            "value": 3.42, "unit": "angstrom", "method": "DFT (PBE)",
            "source": "Hu et al., 2016, JNM", "source_doi": "10.1016/...",
            "confidence": "high", "uncertainty": None, "temperature": 0,
        }
        result = write_ref_value(ref, _existing=existing)
        assert result.status == WriteStatus.DUPLICATE

    def test_full_pipeline_for_umo_bcc(self):
        """Full pipeline: gap → cache miss → mock search → write."""
        # Phase 1: Find gaps
        targets = load_target_systems()
        existing = load_existing_refs([
            {"element_system": "U-Mo", "phase": "BCC", "property": "lattice_constant"},
        ])
        gaps = compute_gaps(targets, existing)
        umo_gaps = [g for g in gaps if g.element_system == "U-Mo"]
        assert len(umo_gaps) >= 7  # 8 properties minus 1 existing

        # Phase 2: Cache query for C11 (miss in this scenario)
        c11_gap = next(g for g in umo_gaps if g.property == "C11")
        cache_result = cache_query(
            c11_gap.element_system, c11_gap.phase, c11_gap.property,
            _l1_rows=[], _l2_params=[],
        )
        assert cache_result is None  # cache miss

        # Phase 3: Simulate extraction result
        extracted = {
            "element_system": "U-Mo", "phase": "BCC", "property": "C11",
            "value": 286.0, "unit": "GPa", "method": "DFT (PBE)",
            "source": "Hu et al., 2016, JNM",
            "source_doi": "10.1016/j.jnucmat.2016.03.032",
            "confidence": "high", "uncertainty": None, "temperature": 0,
        }
        write_result = write_ref_value(extracted, _existing=[])
        assert write_result.status == WriteStatus.WRITTEN_AUTO
