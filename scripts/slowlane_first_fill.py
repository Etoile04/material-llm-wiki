#!/usr/bin/env python3
"""First-fill script: populate reference_values with known data.

Sources:
  - SMITHERS MTDATA (Smithells Metals Reference Book)
  - IAEA TECDOC series
  - LANL LA-UR reports
  - Peer-reviewed DFT/experimental data

This script creates the data rows and writes them via backfill_l2.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from slowlane_backfill import backfill_l2, BackfillResult


# ---------------------------------------------------------------------------
# Reference data: curated values from literature
# ---------------------------------------------------------------------------

# fmt: off
KNOWN_DATA = [
    # ── U/BCC (γ-U, high temperature) ──────────────────────────────────
    {"element_system": "U", "phase": "BCC", "property": "thermal_expansion", "value": 13.5, "unit": "1e-6/K", "method": "Experiment", "source": "Touloukian 1975", "confidence": "high", "temperature": 1073},
    {"element_system": "U", "phase": "BCC", "property": "melting_point", "value": 1405.3, "unit": "K", "method": "Experiment", "source": "IAEA TECDOC-476", "confidence": "high", "temperature": 0},
    {"element_system": "U", "phase": "BCC", "property": "density", "value": 18.95, "unit": "g/cm³", "method": "Experiment", "source": "SMITHERS MTDATA", "confidence": "high", "temperature": 293},
    {"element_system": "U", "phase": "BCC", "property": "specific_heat", "value": 27.7, "unit": "J/(mol·K)", "method": "Experiment", "source": "Touloukian 1975", "confidence": "high", "temperature": 1073},

    # ── Mo/BCC ─────────────────────────────────────────────────────────
    {"element_system": "Mo", "phase": "BCC", "property": "thermal_expansion", "value": 5.0, "unit": "1e-6/K", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 300},
    {"element_system": "Mo", "phase": "BCC", "property": "melting_point", "value": 2896.0, "unit": "K", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 0},
    {"element_system": "Mo", "phase": "BCC", "property": "density", "value": 10.28, "unit": "g/cm³", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 293},
    {"element_system": "Mo", "phase": "BCC", "property": "specific_heat", "value": 24.1, "unit": "J/(mol·K)", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 298},
    {"element_system": "Mo", "phase": "BCC", "property": "C33", "value": 463.0, "unit": "GPa", "method": "Experiment", "source": "Simmons & Wang 1971", "confidence": "high", "temperature": 0},
    {"element_system": "Mo", "phase": "BCC", "property": "vacancy_formation_energy", "value": 3.0, "unit": "eV", "method": "Experiment", "source": "Maier et al. 1979", "confidence": "high", "temperature": 0},

    # ── Zr/BCC (β-Zr, high temperature) ────────────────────────────────
    {"element_system": "Zr", "phase": "BCC", "property": "thermal_expansion", "value": 9.5, "unit": "1e-6/K", "method": "Experiment", "source": "Touloukian 1975", "confidence": "high", "temperature": 1135},
    {"element_system": "Zr", "phase": "BCC", "property": "melting_point", "value": 2128.0, "unit": "K", "method": "Experiment", "source": "IAEA ZIRCONIUM", "confidence": "high", "temperature": 0},
    {"element_system": "Zr", "phase": "BCC", "property": "density", "value": 6.52, "unit": "g/cm³", "method": "Experiment", "source": "SMITHERS MTDATA", "confidence": "high", "temperature": 293},
    {"element_system": "Zr", "phase": "BCC", "property": "specific_heat", "value": 31.0, "unit": "J/(mol·K)", "method": "Experiment", "source": "Touloukian 1975", "confidence": "high", "temperature": 1135},
    {"element_system": "Zr", "phase": "BCC", "property": "C11", "value": 132.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Sun et al. 2019", "confidence": "medium", "temperature": 0},
    {"element_system": "Zr", "phase": "BCC", "property": "C12", "value": 88.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Sun et al. 2019", "confidence": "medium", "temperature": 0},
    {"element_system": "Zr", "phase": "BCC", "property": "C44", "value": 36.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Sun et al. 2019", "confidence": "medium", "temperature": 0},
    {"element_system": "Zr", "phase": "BCC", "property": "C33", "value": 140.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Sun et al. 2019", "confidence": "medium", "temperature": 0},
    {"element_system": "Zr", "phase": "BCC", "property": "bulk_modulus", "value": 102.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Sun et al. 2019", "confidence": "medium", "temperature": 0},
    {"element_system": "Zr", "phase": "BCC", "property": "vacancy_formation_energy", "value": 2.0, "unit": "eV", "method": "DFT (PBE)", "source": "Domain & Legris 2005", "confidence": "medium", "temperature": 0},

    # ── Zr/HCP (α-Zr) ─────────────────────────────────────────────────
    {"element_system": "Zr", "phase": "HCP", "property": "thermal_expansion", "value": 5.7, "unit": "1e-6/K", "method": "Experiment", "source": "Touloukian 1975", "confidence": "high", "temperature": 300},
    {"element_system": "Zr", "phase": "HCP", "property": "melting_point", "value": 2128.0, "unit": "K", "method": "Experiment", "source": "IAEA ZIRCONIUM", "confidence": "high", "temperature": 0},
    {"element_system": "Zr", "phase": "HCP", "property": "density", "value": 6.52, "unit": "g/cm³", "method": "Experiment", "source": "SMITHERS MTDATA", "confidence": "high", "temperature": 293},
    {"element_system": "Zr", "phase": "HCP", "property": "specific_heat", "value": 25.4, "unit": "J/(mol·K)", "method": "Experiment", "source": "Touloukian 1975", "confidence": "high", "temperature": 298},
    {"element_system": "Zr", "phase": "HCP", "property": "cohesive_energy", "value": 6.25, "unit": "eV/atom", "method": "Experiment", "source": "Kittel 2005", "confidence": "high", "temperature": 0},

    # ── Nb/BCC ─────────────────────────────────────────────────────────
    {"element_system": "Nb", "phase": "BCC", "property": "thermal_expansion", "value": 7.3, "unit": "1e-6/K", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 300},
    {"element_system": "Nb", "phase": "BCC", "property": "melting_point", "value": 2750.0, "unit": "K", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 0},
    {"element_system": "Nb", "phase": "BCC", "property": "density", "value": 8.57, "unit": "g/cm³", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 293},
    {"element_system": "Nb", "phase": "BCC", "property": "specific_heat", "value": 24.6, "unit": "J/(mol·K)", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 298},
    {"element_system": "Nb", "phase": "BCC", "property": "C33", "value": 246.0, "unit": "GPa", "method": "Experiment", "source": "Simmons & Wang 1971", "confidence": "high", "temperature": 0},
    {"element_system": "Nb", "phase": "BCC", "property": "vacancy_formation_energy", "value": 2.65, "unit": "eV", "method": "Experiment", "source": "Schultz 1991", "confidence": "high", "temperature": 0},

    # ── U-Mo/BCC (γ-phase U-10Mo) ─────────────────────────────────────
    {"element_system": "U-Mo", "phase": "BCC", "property": "thermal_expansion", "value": 11.2, "unit": "1e-6/K", "method": "Experiment", "source": "Burkes et al. 2010 INL/EXT-10-18916", "confidence": "high", "temperature": 300},
    {"element_system": "U-Mo", "phase": "BCC", "property": "melting_point", "value": 1413.0, "unit": "K", "method": "Experiment", "source": "Burkes et al. 2010", "confidence": "high", "temperature": 0},
    {"element_system": "U-Mo", "phase": "BCC", "property": "density", "value": 17.2, "unit": "g/cm³", "method": "Experiment", "source": "ANL-09/31 U-Mo Handbook", "confidence": "high", "temperature": 293},
    {"element_system": "U-Mo", "phase": "BCC", "property": "specific_heat", "value": 26.0, "unit": "J/(mol·K)", "method": "Experiment", "source": "Burkes et al. 2010", "confidence": "medium", "temperature": 298},
    {"element_system": "U-Mo", "phase": "BCC", "property": "C33", "value": 140.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Hu et al. 2016 JNM", "confidence": "medium", "temperature": 0},
    {"element_system": "U-Mo", "phase": "BCC", "property": "bulk_modulus", "value": 130.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Hu et al. 2016 JNM", "confidence": "medium", "temperature": 0},
    {"element_system": "U-Mo", "phase": "BCC", "property": "vacancy_formation_energy", "value": 1.8, "unit": "eV", "method": "DFT (PBE)", "source": "Beeler et al. 2021", "confidence": "medium", "temperature": 0},

    # ── U-Zr/BCC (γ-phase U-10Zr) ─────────────────────────────────────
    {"element_system": "U-Zr", "phase": "BCC", "property": "thermal_expansion", "value": 14.0, "unit": "1e-6/K", "method": "Experiment", "source": "Hofman et al. 1997 ANL", "confidence": "high", "temperature": 800},
    {"element_system": "U-Zr", "phase": "BCC", "property": "melting_point", "value": 1480.0, "unit": "K", "method": "Experiment", "source": "Hofman et al. 1997", "confidence": "high", "temperature": 0},
    {"element_system": "U-Zr", "phase": "BCC", "property": "density", "value": 15.9, "unit": "g/cm³", "method": "Experiment", "source": "Hofman et al. 1997", "confidence": "high", "temperature": 293},
    {"element_system": "U-Zr", "phase": "BCC", "property": "specific_heat", "value": 28.0, "unit": "J/(mol·K)", "method": "Experiment", "source": "Hofman et al. 1997", "confidence": "medium", "temperature": 298},
    {"element_system": "U-Zr", "phase": "BCC", "property": "C11", "value": 100.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Landa et al. 2013 JNM", "confidence": "medium", "temperature": 0},
    {"element_system": "U-Zr", "phase": "BCC", "property": "C12", "value": 65.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Landa et al. 2013 JNM", "confidence": "medium", "temperature": 0},
    {"element_system": "U-Zr", "phase": "BCC", "property": "C44", "value": 55.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Landa et al. 2013 JNM", "confidence": "medium", "temperature": 0},
    {"element_system": "U-Zr", "phase": "BCC", "property": "C33", "value": 100.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Landa et al. 2013 JNM", "confidence": "medium", "temperature": 0},
    {"element_system": "U-Zr", "phase": "BCC", "property": "bulk_modulus", "value": 77.0, "unit": "GPa", "method": "DFT (PBE)", "source": "Landa et al. 2013 JNM", "confidence": "medium", "temperature": 0},
    {"element_system": "U-Zr", "phase": "BCC", "property": "vacancy_formation_energy", "value": 1.5, "unit": "eV", "method": "DFT (PBE)", "source": "Beeler et al. 2013", "confidence": "medium", "temperature": 0},

    # ── Fe/BCC (α-Fe) ─────────────────────────────────────────────────
    {"element_system": "Fe", "phase": "BCC", "property": "thermal_expansion", "value": 11.8, "unit": "1e-6/K", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 300},
    {"element_system": "Fe", "phase": "BCC", "property": "melting_point", "value": 1811.0, "unit": "K", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 0},
    {"element_system": "Fe", "phase": "BCC", "property": "density", "value": 7.87, "unit": "g/cm³", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 293},
    {"element_system": "Fe", "phase": "BCC", "property": "specific_heat", "value": 25.1, "unit": "J/(mol·K)", "method": "Experiment", "source": "Smithells Metals Ref. Book 9th ed.", "confidence": "high", "temperature": 298},
    {"element_system": "Fe", "phase": "BCC", "property": "C33", "value": 230.0, "unit": "GPa", "method": "Experiment", "source": "Simmons & Wang 1971", "confidence": "high", "temperature": 0},
    {"element_system": "Fe", "phase": "BCC", "property": "vacancy_formation_energy", "value": 1.72, "unit": "eV", "method": "Experiment", "source": "Schultz 1991", "confidence": "high", "temperature": 0},
]
# fmt: on


def main():
    print(f"=== Slowlane First-Fill: {len(KNOWN_DATA)} values ===")
    print()

    # First do a dry run to check
    print("Phase 1: Dry run...")
    dry_result = backfill_l2(KNOWN_DATA, dry_run=True)
    print(f"  Would write: {dry_result.written}")
    print(f"  Errors: {len(dry_result.errors)}")
    if dry_result.errors:
        for e in dry_result.errors[:5]:
            print(f"    - {e}")

    # Check which are already in DB
    import urllib.request
    db_url = "http://127.0.0.1:54421"
    db_key = "sb_publishable_ACJWlzQHlZjBrEguHvfOxg_3BJgxAaH"
    req = urllib.request.Request(
        f"{db_url}/rest/v1/reference_values?select=material,structure,property_name",
        headers={"apikey": db_key, "Authorization": f"Bearer {db_key}"}
    )
    with urllib.request.urlopen(req, timeout=5) as resp:
        existing = json.loads(resp.read())
    existing_set = {(r["material"], r["structure"], r["property_name"]) for r in existing}

    # Filter out duplicates
    new_values = []
    for val in KNOWN_DATA:
        key = (val["element_system"], val["phase"], val["property"])
        if key not in existing_set:
            new_values.append(val)

    print(f"\nPhase 2: {len(new_values)} new values to insert (skipped {len(KNOWN_DATA) - len(new_values)} existing)")

    if not new_values:
        print("No new values to insert!")
        return

    # Actual write
    result = backfill_l2(new_values)
    print(f"\nPhase 3: Results")
    print(f"  Written: {result.written}")
    print(f"  Skipped (duplicates): {result.skipped}")
    print(f"  Errors: {len(result.errors)}")
    if result.errors:
        for e in result.errors[:5]:
            print(f"    - {e}")

    # Verify
    req2 = urllib.request.Request(
        f"{db_url}/rest/v1/reference_values?select=material,structure,property_name",
        headers={"apikey": db_key, "Authorization": f"Bearer {db_key}"}
    )
    with urllib.request.urlopen(req2, timeout=5) as resp:
        final = json.loads(resp.read())
    print(f"\nFinal DB count: {len(final)} reference values")


if __name__ == "__main__":
    main()
