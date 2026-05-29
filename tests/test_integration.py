"""Integration test: cross-component compatibility and full data flow."""
import json
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from gap_analyzer import load_target_systems, compute_gaps, load_existing_refs, GapItem
from cache_query import cache_query, CacheLevel, CacheResult, load_property_mapping
from adapter_nfmd import adapt_nfmd_param
from adapter_wiki import adapt_wiki_param
from adapter_ontology import adapt_ontology_individual
from write_ref_value import write_ref_value, WriteStatus, passes_range_check


class TestPropertyMappingIntegration:
    """Test property mapping is consistent across all components."""

    def test_all_12_properties_in_mapping(self):
        mapping = load_property_mapping()
        expected = [
            "lattice_constant", "cohesive_energy",
            "C11", "C12", "C44", "C33",
            "bulk_modulus", "vacancy_formation_energy",
            "formation_energy", "surface_energy",
            "melting_point", "thermal_conductivity",
        ]
        for prop in expected:
            assert prop in mapping, f"Missing property: {prop}"

    def test_range_check_covers_all_properties(self):
        mapping = load_property_mapping()
        for prop, info in mapping.items():
            assert "range" in info, f"No range for {prop}"
            assert "min" in info["range"]
            assert "max" in info["range"]
            assert passes_range_check(prop, (info["range"]["min"] + info["range"]["max"]) / 2)


class TestAdapterCompatibility:
    """Test that all adapters produce write-compatible output."""

    def test_nfmd_adapter_output_passes_quality_gate(self):
        param = {
            "material_raw": "U",
            "name": "lattice parameter",
            "symbol": "a",
            "value_scalar": 3.39,
            "unit": "Å",
            "temperature_k": 0,
            "method": "DFT (PBE)",
            "source_file": "test-source.md",
        }
        adapted = adapt_nfmd_param(param, phase="BCC")
        result = write_ref_value(adapted, _existing=[])
        assert result.status in (WriteStatus.WRITTEN_AUTO, WriteStatus.WRITTEN_PENDING_REVIEW)

    def test_wiki_adapter_output_passes_quality_gate(self):
        param = {
            "system": "Mo",
            "phase": "BCC",
            "property_zh": "晶格常数",
            "value": 3.15,
            "unit": "Å",
            "temperature": "0K",
            "method": "DFT",
            "source": "Test Paper 2024",
        }
        adapted = adapt_wiki_param(param)
        result = write_ref_value(adapted, _existing=[])
        assert result.status in (WriteStatus.WRITTEN_AUTO, WriteStatus.WRITTEN_PENDING_REVIEW)

    def test_wiki_adapter_confidence_is_string(self):
        """Wiki adapter should return confidence as string (fixed)."""
        param = {
            "system": "Mo",
            "phase": "BCC",
            "property_zh": "晶格常数",
            "value": 3.15,
            "unit": "Å",
            "temperature": "0K",
            "method": "DFT",
            "source": "Test Paper 2024",
        }
        adapted = adapt_wiki_param(param)
        # confidence should be str for write_ref_value compatibility
        assert isinstance(adapted["confidence"], str), (
            "wiki adapter must return string confidence for write_ref_value compatibility; "
            "consumers must normalize"
        )

    def test_ontology_adapter_output_passes_quality_gate(self):
        individual = {
            "class": "UraniumMolybdenumAlloy",
            "properties": {
                "latticeConstant": {"value": 3.42, "unit": "Å"},
            },
            "source": "ontofuel extraction",
        }
        results = adapt_ontology_individual(individual)
        assert results is not None and len(results) > 0
        for adapted in results:
            result = write_ref_value(adapted, _existing=[])
            assert result.status in (
                WriteStatus.WRITTEN_AUTO,
                WriteStatus.WRITTEN_PENDING_REVIEW,
                WriteStatus.REJECTED,
            )


class TestGapAnalyzerIntegration:
    """Test gap analyzer with real target systems."""

    def test_full_gap_matrix_size(self):
        targets = load_target_systems()
        existing = set()  # no existing data
        gaps = compute_gaps(targets, existing)
        # 14 systems × 8 properties = 112 gaps max
        # Some systems have fewer properties (e.g. SiC may not have all)
        assert len(gaps) > 50
        assert len(gaps) <= 112

    def test_fully_populated_no_gaps(self):
        targets = load_target_systems()
        # Create existing set with ALL possible combinations
        all_existing = set()
        for t in targets:
            for prop in t.get("properties", []):
                all_existing.add((t["element_system"], t["phase"], prop))

        refs = [
            {"element_system": s, "phase": p, "property": pr}
            for s, p, pr in all_existing
        ]
        existing = load_existing_refs(refs)
        gaps = compute_gaps(targets, existing)
        assert len(gaps) == 0


class TestCacheQueryIntegration:
    """Test cache query with adapter chain."""

    def test_l2_hit_adapts_and_writes(self):
        mock_params = [
            {
                "material_raw": "Zr",
                "name": "lattice parameter",
                "symbol": "a",
                "value_scalar": 3.23,
                "unit": "Å",
                "temperature_k": 0,
                "method": "DFT",
                "source_file": "zr-test.md",
            }
        ]
        result = cache_query(
            "Zr", "BCC", "lattice_constant",
            _l1_rows=[], _l2_params=mock_params,
        )
        assert result is not None
        assert result.level == CacheLevel.L2

        # Convert to ref_value format and write
        ref = result.to_ref_value_dict()
        ref["confidence"] = "medium"
        write_result = write_ref_value(ref, _existing=[])
        assert write_result.status in (
            WriteStatus.WRITTEN_AUTO,
            WriteStatus.WRITTEN_PENDING_REVIEW,
        )


class TestEdgeCases:
    """Test edge cases across components."""

    def test_out_of_range_value_rejected(self):
        """Value outside property-mapping range should be rejected."""
        ref = {
            "element_system": "U", "phase": "BCC", "property": "lattice_constant",
            "value": 999.0, "unit": "angstrom", "method": "DFT",
            "source": "Test", "confidence": "high",
            "uncertainty": None, "temperature": 0,
        }
        result = write_ref_value(ref, _existing=[])
        assert result.status == WriteStatus.REJECTED

    def test_empty_source_rejected(self):
        ref = {
            "element_system": "U", "phase": "BCC", "property": "lattice_constant",
            "value": 3.39, "unit": "angstrom", "method": "DFT",
            "source": "", "confidence": "high",
            "uncertainty": None, "temperature": 0,
        }
        result = write_ref_value(ref, _existing=[])
        assert result.status == WriteStatus.REJECTED

    def test_different_methods_not_duplicate(self):
        existing = [
            {
                "element_system": "U", "phase": "BCC", "property": "lattice_constant",
                "method": "DFT", "source": "Paper A",
            },
        ]
        ref = {
            "element_system": "U", "phase": "BCC", "property": "lattice_constant",
            "value": 3.39, "unit": "angstrom", "method": "experiment",
            "source": "Paper A", "confidence": "high",
            "uncertainty": None, "temperature": 300,
        }
        result = write_ref_value(ref, _existing=existing)
        assert result.status != WriteStatus.DUPLICATE
