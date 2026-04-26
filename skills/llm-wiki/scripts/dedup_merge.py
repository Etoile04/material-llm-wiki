#!/usr/bin/env python3
"""
Deduplication and merge script for fuel_swelling_wiki summaries and parameters.
Performs safe merge: keep larger, merge unique params from smaller, delete smaller.
"""

import json
import os
import shutil
from pathlib import Path
from collections import defaultdict

WIKI_ROOT = Path("/Users/lwj04/.openclaw/workspace/data/fuel_swelling_wiki")
SUMMARIES_DIR = WIKI_ROOT / "wiki" / "summaries"
PARAMS_DIR = WIKI_ROOT / "parameters"
INDEX_PATH = WIKI_ROOT / "wiki" / "index.md"

# Stats
stats = {
    "groups_merged": 0,
    "summaries_deleted": 0,
    "params_deleted": 0,
    "params_before_total": 0,
    "params_after_total": 0,
    "params_merged_in": 0,
    "uncertain_groups": [],
    "kept_both": [],
    "redirects": {},  # old_slug -> new_slug
}


def read_params(slug):
    """Read parameter JSON file, return list or empty list."""
    path = PARAMS_DIR / f"{slug}.json"
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    return []


def write_params(slug, data):
    """Write parameter JSON file."""
    path = PARAMS_DIR / f"{slug}.json"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def delete_summary(slug):
    """Delete summary .md file."""
    path = SUMMARIES_DIR / f"{slug}.md"
    if path.exists():
        path.unlink()
        stats["summaries_deleted"] += 1
        print(f"  [DEL] summary: {slug}.md")
    # Also check for summary directory
    dirpath = SUMMARIES_DIR / slug
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)
        print(f"  [DEL] summary dir: {slug}/")


def delete_params(slug):
    """Delete parameter JSON file."""
    path = PARAMS_DIR / f"{slug}.json"
    if path.exists():
        path.unlink()
        stats["params_deleted"] += 1
        print(f"  [DEL] params: {slug}.json")


def merge_params(keep_slug, merge_slug):
    """Merge unique params from merge_slug into keep_slug. Returns number of new params added."""
    keep_data = read_params(keep_slug)
    merge_data = read_params(merge_slug)

    stats["params_before_total"] += len(keep_data) + len(merge_data)

    # Build dedup key set from keep
    def param_key(p):
        return (p.get('symbol', ''), p.get('material', ''), p.get('temperature', ''))

    existing_keys = set(param_key(p) for p in keep_data)
    added = 0
    for p in merge_data:
        key = param_key(p)
        if key not in existing_keys:
            p['source_file'] = f'summaries/{keep_slug}.md'
            keep_data.append(p)
            existing_keys.add(key)
            added += 1

    # Update source_file for all params
    for p in keep_data:
        p['source_file'] = f'summaries/{keep_slug}.md'

    write_params(keep_slug, keep_data)
    stats["params_after_total"] += len(keep_data)
    stats["params_merged_in"] += added

    print(f"  [MERGE] {merge_slug}: {len(merge_data)} params -> kept {keep_slug} (added {added} new, total now {len(keep_data)})")
    return added


def do_merge(keep_slug, merge_slugs):
    """Perform full merge: params + delete summaries & params."""
    print(f"\n[MERGE GROUP] keep={keep_slug}, merge={merge_slugs}")
    
    for merge_slug in merge_slugs:
        merge_params(keep_slug, merge_slug)
        delete_summary(merge_slug)
        delete_params(merge_slug)
        stats["redirects"][merge_slug] = keep_slug
    
    stats["groups_merged"] += 1


# ============================================================
# DECISIONS based on file analysis
# ============================================================

# Group 1: Ronchi 1979 — SAME PAPER (same topic, Ronchi 1979 fission gas swelling MX fuels)
do_merge("1979_Ronchi_FissionGasSwellingMX_Fuels", [
    "1979_Ronchi_FissionGasSwelling_Physics",
])

# Group 2: Hofman 1990 — SAME PAPER
do_merge("1990_Hofman_SwellingBehaviorUPuZr", [
    "1990_Hofman_Swelling_UPuZr",
])

# Group 3: Rest 1993 — DIFFERENT PAPERS (different journals: JNM 207 vs ASTM STP 1175)
# VoidSwelling = JNM paper; CavitationalSwelling = ASTM conference paper
# KEEP BOTH
print("\n[KEEP BOTH] Rest 1993: VoidSwellingAlphaU (JNM 207) vs CavitationalSwellingAlphaUPuZr (ASTM STP 1175) — different papers")
stats["kept_both"].append("Rest 1993: two different publications")

# Group 4: Ogata 1996 — SAME PAPER (same authors, same journal JNM 230, pp 129-139)
# Keep the larger English summary, merge params from the Chinese one
do_merge("1996_Ogata_FissionGasBehavior_MetallicFuel", [
    "1996_Ogata_FissionGasMetallic_Analytical",
])

# Group 5: Rest 2005 — SAME PAPER
do_merge("2005_Rest_RecrystallizationSwellingUO2UMo", [
    "2005_Rest_IrradiationInducedRecrystallization",
])

# Group 6: Kim 2011 — SAME PAPER
do_merge("2011_Kim_FissionProductInducedSwellingUMo", [
    "2011_Kim_FissionProductSwelling_UMo",
])

# Group 7: Karahan 2013 — 3 files, SAME PAPER (FEAST METAL fuel swelling model)
# Keep: 2013_Karahan_FEAST_ExtendedSwelling_UPuZr (most params: 30)
# Actually the task says keep the one with most params. Let's check sizes:
# ExtendedSwelling_UPuZr: 30 params, FEAST_METAL_FuelSwelling: 24 params, METAL_ExtendedSwelling: 18 params
# Keep ExtendedSwelling_UPuZr (30 params is most)
do_merge("2013_Karahan_FEAST_ExtendedSwelling_UPuZr", [
    "2013_Karahan_FEAST_METAL_FuelSwelling",
    "2013_Karahan_FEAST_METAL_ExtendedSwelling",
])

# Group 8: Kim 2013 — 6 files, 2 DIFFERENT PAPERS
# Paper A: "Fission induced swelling and creep of U-Mo alloy fuel" (JNM 437, 37-46)
#   - 2013_Kim_FissionInducedSwellingCreepUMo (10255B, 16 params) — KEEP (largest)
#   - 2013_Kim_FissionInducedSwellingCreep_UMo (3835B, 11 params)
#   - 2013_Kim_SwellingCreep_UMo (3317B, 15 params)
# Paper B: "Recrystallization and fission-gas-bubble swelling of U-Mo fuel" (JNM 436, 14-22)
#   - 2013_Kim_RecrystallizationFGBSwellingUMo (5414B) — KEEP (largest, no params file)
#   - 2013_Kim_RecrystallizationFGBSwelling_UMo (3870B, 14 params)
#   - 2013_Kim_Recrystallization_FGBSwelling_UMo (3888B, 25 params) — most params

# For Paper B, RecrystallizationFGBSwellingUMo has no params file.
# Recrystallization_FGBSwelling_UMo has 25 params (most). Keep that one.
# Actually let's keep RecrystallizationFGBSwellingUMo (largest summary) and merge params from the other two

do_merge("2013_Kim_FissionInducedSwellingCreepUMo", [
    "2013_Kim_FissionInducedSwellingCreep_UMo",
    "2013_Kim_SwellingCreep_UMo",
])

# Paper B: Keep RecrystallizationFGBSwellingUMo (largest summary, 5414B)
# but it has no params file. Merge params from the other two.
# First, let's copy params from the one with most params as the base
print("\n[Group 8 Paper B] Kim 2013 Recrystallization papers")
# RecrystallizationFGBSwellingUMo has NO params file. 
# Recrystallization_FGBSwelling_UMo has 25 params (most).
# Strategy: use _FGBSwelling_UMo's params as base, copy to RecrystallizationFGBSwellingUMo,
# then merge RecrystallizationFGBSwelling_UMo params in
base_params = read_params("2013_Kim_Recrystallization_FGBSwelling_UMo")
for p in base_params:
    p['source_file'] = f'summaries/2013_Kim_RecrystallizationFGBSwellingUMo.md'
write_params("2013_Kim_RecrystallizationFGBSwellingUMo", base_params)
print(f"  [CREATE] params for 2013_Kim_RecrystallizationFGBSwellingUMo from _FGBSwelling_UMo ({len(base_params)} params)")

# Now merge the other one into it
merge_params("2013_Kim_RecrystallizationFGBSwellingUMo", "2013_Kim_RecrystallizationFGBSwelling_UMo")

# Delete the smaller ones
delete_summary("2013_Kim_RecrystallizationFGBSwelling_UMo")
delete_params("2013_Kim_RecrystallizationFGBSwelling_UMo")
stats["redirects"]["2013_Kim_RecrystallizationFGBSwelling_UMo"] = "2013_Kim_RecrystallizationFGBSwellingUMo"

delete_summary("2013_Kim_Recrystallization_FGBSwelling_UMo")
delete_params("2013_Kim_Recrystallization_FGBSwelling_UMo")
stats["redirects"]["2013_Kim_Recrystallization_FGBSwelling_UMo"] = "2013_Kim_RecrystallizationFGBSwellingUMo"
stats["groups_merged"] += 1

# Group 9: Cui 2015 — SAME PAPER
do_merge("2015_Cui_MechanisticGaseousSwellingUMo", [
    "2015_Cui_MechanisticGaseousSwelling",
])

# Group 10: Hu 2016 — GrainMorphology has two versions (same paper)
# 2016_Hu_GrainMorphologyGasBubbleUMo (6364B, 28 params) — KEEP (larger)
# 2016_Hu_GrainMorphology_BubbleSwelling_UMo_BoothModel (4072B, 4 params)
# 2016_Hu_GasBubbleSuperlatticeFormationPF — DIFFERENT PAPER (gas bubble superlattice formation, phase field)
do_merge("2016_Hu_GrainMorphologyGasBubbleUMo", [
    "2016_Hu_GrainMorphology_BubbleSwelling_UMo_BoothModel",
])
print("[KEEP] 2016_Hu_GasBubbleSuperlatticeFormationPF — different paper (phase field superlattice)")

# Group 11: Beeler 2020 — RadiationDrivenDiffusion
# 2020_Beeler_ImprovedEOSXeBubbleUMo — DIFFERENT PAPER (Xe bubble EOS)
# 2020_Beeler_RadiationDrivenDiffusion_UMo (6468B) — KEEP (larger)
# 2020_Beeler_RadiationDrivenDiffusionUMo (3670B) — also exists
# 2021_Beeler_RadiationDrivenDiffusionUMo — same paper, different year slug
# Note: the "2021" version has same title "Radiation driven diffusion in γU-Mo"
# Let's keep 2020_Beeler_RadiationDrivenDiffusion_UMo (largest summary) and merge the other two
do_merge("2020_Beeler_RadiationDrivenDiffusion_UMo", [
    "2020_Beeler_RadiationDrivenDiffusionUMo",
    "2021_Beeler_RadiationDrivenDiffusionUMo",
])
print("[KEEP] 2020_Beeler_ImprovedEOSXeBubbleUMo — different paper (Xe EOS)")

# Group 12: Hilty 2021 — SAME PAPER
do_merge("2021_Hilty_FissionGasBubblesThermalConductivity", [
    "2021_Hilty_FGBubble_ThermalConductivity",
])

# Group 13: Robinson 2021 — SAME PAPER
do_merge("2021_Robinson_PredictiveSwellingUMoMonolithic", [
    "2021_Robinson_SwellingCorrelation_UMo",
])

# Group 14: Zhang 2021 — SAME PAPER
do_merge("2021_Zhang_EffectiveSwellingInertMatrix", [
    "2021_Zhang_EffectiveIrradiationSwelling",
])

# Group 15: Smith 2023 — DIFFERENT PAPERS, keep both
print("\n[KEEP BOTH] Smith 2023: UCInclusionsGBS and EarlySelfOrganizationGBS — different papers")
stats["kept_both"].append("Smith 2023: two different papers")

# Group 16: Ye 2023 — SAME PAPER
do_merge("2023_Ye_IntegratedSimulationU10Mo", [
    "2023_Ye_IntegratedSimulation_U10Mo_Swelling",
])

# Group 17: Muntaha 2024 — SAME PAPER
do_merge("2024_Muntaha_GB_SurfaceDiffusion", [
    "2024_Muntaha_GBSDiffusion_FGBubbleRelease",
])

# Group 18: Aagesen 2025 — SAME PAPER (all three have same authors: Aagesen, Zhang, Jiang, Gan)
# PhaseTransformation_Superlattice (5462B, no params) — largest summary, English
# VoidSuperlattice_Mo (4502B, no params) — Chinese version  
# SuperlatticePhaseTransformation (4235B, has params) — has params
# Keep PhaseTransformation_Superlattice (largest), merge params from SuperlatticePhaseTransformation
print("\n[Group 18] Aagesen 2025")
# SuperlatticePhaseTransformation has params
aagesen_params = read_params("2025_Aagesen_SuperlatticePhaseTransformation")
for p in aagesen_params:
    p['source_file'] = f'summaries/2025_Aagesen_PhaseTransformation_Superlattice.md'
write_params("2025_Aagesen_PhaseTransformation_Superlattice", aagesen_params)
print(f"  [CREATE] params for PhaseTransformation_Superlattice from SuperlatticePhaseTransformation ({len(aagesen_params)} params)")

delete_summary("2025_Aagesen_VoidSuperlattice_Mo")
delete_summary("2025_Aagesen_SuperlatticePhaseTransformation")
delete_params("2025_Aagesen_SuperlatticePhaseTransformation")
stats["summaries_deleted"] += 2
stats["params_deleted"] += 1
stats["redirects"]["2025_Aagesen_VoidSuperlattice_Mo"] = "2025_Aagesen_PhaseTransformation_Superlattice"
stats["redirects"]["2025_Aagesen_SuperlatticePhaseTransformation"] = "2025_Aagesen_PhaseTransformation_Superlattice"
stats["groups_merged"] += 1

# Group 19: Hanson 2025 — SAME PAPER
do_merge("2025_Hanson_StablePredictableSwellingU10Mo", [
    "2025_Hanson_StableSwelling_U10Mo",
])

# Group 20: Li 2023 — only one summary file exists (ElasticConstantsU10Mo)
# but two param files exist. The EffectiveElasticConstants_IrradiatedU10Mo summary doesn't exist
# This means the second params file is orphaned. Merge params into the existing one.
print("\n[Group 20] Li 2023 — only one summary, two param files")
merge_params("2023_Li_ElasticConstantsU10Mo", "2023_Li_EffectiveElasticConstants_IrradiatedU10Mo")
delete_params("2023_Li_EffectiveElasticConstants_IrradiatedU10Mo")
stats["redirects"]["2023_Li_EffectiveElasticConstants_IrradiatedU10Mo"] = "2023_Li_ElasticConstantsU10Mo"
stats["groups_merged"] += 1

# Also clean up orphaned Ogata params file
print("\n[CLEANUP] Orphaned Ogata_1996_FissionGasMetallic_Analytical.json")
orphan_path = PARAMS_DIR / "Ogata_1996_FissionGasMetallic_Analytical.json"
if orphan_path.exists():
    # Check if this is just a duplicate with different naming
    orphan_data = read_params("Ogata_1996_FissionGasMetallic_Analytical")
    if orphan_data:
        merge_params("1996_Ogata_FissionGasBehavior_MetallicFuel", "Ogata_1996_FissionGasMetallic_Analytical")
    delete_params("Ogata_1996_FissionGasMetallic_Analytical")

# ============================================================
# Now update index.md
# ============================================================
print("\n\n=== Updating index.md ===")

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Build replacement map for index.md
# Replace wiki links to deleted slugs with kept slugs
for old_slug, new_slug in stats["redirects"].items():
    # Replace wiki link references: [[wiki/summaries/OLD_SLUG|...]] -> [[wiki/summaries/NEW_SLUG|...]]
    import re
    # Pattern: [[wiki/summaries/OLD_SLUG|anything]] or [[wiki/summaries/OLD_SLUG]]
    index_content = re.sub(
        rf'\[\[wiki/summaries/{re.escape(old_slug)}(\|[^\]]*)?\]\]',
        rf'[[wiki/summaries/{new_slug}\1]]',
        index_content
    )

# Remove duplicate lines in index (after redirects, there might be two links to same slug)
lines = index_content.split('\n')
seen_summary_lines = set()
deduped_lines = []
for line in lines:
    # Only deduplicate summary link lines
    if '[[wiki/summaries/' in line and line.strip().startswith('-'):
        # Normalize for comparison
        normalized = line.strip()
        if normalized in seen_summary_lines:
            print(f"  [DEDUP LINE] removing duplicate: {line.strip()[:80]}...")
            continue
        seen_summary_lines.add(normalized)
    deduped_lines.append(line)

index_content = '\n'.join(deduped_lines)

# Now also clean up the Batch sections at the bottom that reference deleted slugs
# Replace references in batch sections
for old_slug, new_slug in stats["redirects"].items():
    # Also replace in batch section text references
    index_content = index_content.replace(old_slug, new_slug)

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("  [UPDATED] index.md")

# ============================================================
# Update cross-references in all remaining summaries
# ============================================================
print("\n=== Updating cross-references in summaries ===")

# Find all remaining summary files
remaining_summaries = [f for f in SUMMARIES_DIR.iterdir() if f.suffix == '.md' and f.is_file()]
cross_ref_count = 0

for summary_path in remaining_summaries:
    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old_slug, new_slug in stats["redirects"].items():
        if old_slug in content:
            content = content.replace(old_slug, new_slug)
            modified = True
    
    if modified:
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(content)
        cross_ref_count += 1
        print(f"  [XREF] updated cross-refs in {summary_path.name}")

print(f"  Updated cross-references in {cross_ref_count} files")

# ============================================================
# Final Report
# ============================================================
print("\n" + "="*60)
print("DEDUPLICATION COMPLETE")
print("="*60)
print(f"Groups merged: {stats['groups_merged']}")
print(f"Summaries deleted: {stats['summaries_deleted']}")
print(f"Parameter files deleted: {stats['params_deleted']}")
print(f"New params merged in (deduplicated): {stats['params_merged_in']}")
print(f"Groups kept as-is (different papers): {len(stats['kept_both'])}")
print(f"Cross-reference files updated: {cross_ref_count}")
print(f"\nKept both (not same paper):")
for item in stats["kept_both"]:
    print(f"  - {item}")
print(f"\nRedirects (old -> new):")
for old, new in stats["redirects"].items():
    print(f"  {old} -> {new}")
