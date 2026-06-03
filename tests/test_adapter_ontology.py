"""Test ontofuel individual → reference_value adapter."""
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from adapter_ontology import adapt_ontology_individual, OntologyAdapterError


def test_density_now_mapped_returns_data():
    """Density is now a target property (Phase 2), should return data."""
    individual = {
        "class": "Uranium",
        "properties": {
            "hasDensity": {"value": 19.1, "unit": "g/cm³"},
        },
        "source": "ontofuel extraction",
    }
    result = adapt_ontology_individual(individual)
    assert result is not None
    assert len(result) > 0
    assert any(r["property"] == "density" for r in result)


def test_lattice_constant_mapping():
    individual = {
        "class": "UraniumMolybdenumAlloy",
        "properties": {
            "latticeConstant": {"value": 3.39, "unit": "Å"},
        },
        "source": "ontofuel extraction",
    }
    results = adapt_ontology_individual(individual)
    assert results is not None
    assert len(results) > 0
    assert any(r["property"] == "lattice_constant" for r in results)


def test_formation_energy_not_mapped_returns_none():
    """formation_energy is not in property-mapping.json, should return none."""
    individual = {
        "class": "UraniumZirconiumAlloy",
        "properties": {
            "formationEnergy": {"value": -0.15, "unit": "eV/atom"},
        },
        "source": "ontofuel extraction",
    }
    results = adapt_ontology_individual(individual)
    # formation_energy is not a target property — should return empty or None
    assert results is None or len(results) == 0


def test_empty_properties_returns_none():
    individual = {
        "class": "Uranium",
        "properties": {},
        "source": "test",
    }
    result = adapt_ontology_individual(individual)
    assert result is None or len(result) == 0
