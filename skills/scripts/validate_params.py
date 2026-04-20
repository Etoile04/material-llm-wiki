#!/usr/bin/env python3
"""Validate extracted material parameter JSON files for quality issues."""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

# category-level defaults (broad); subcategory overrides below
RANGES = {
    'diffusion': {'min': 1e-30, 'max': 1e+25},
    'bubble': {'min': 1e-15, 'max': 1e+25},
    'swelling_rate': {'min': 1e-10, 'max': 1e+3},
    'rate_theory': {'min': 1e-30, 'max': 1e+30},
    'surface_energy': {'min': 0.01, 'max': 10.0},
    'thermal': {'min': 0.1, 'max': 1000.0},
    'mechanical': {'min': 1e6, 'max': 1e12},
    'recrystallization': {'min': 1e20, 'max': 1e30},
    'microstructure': {'min': 1e-10, 'max': 1e+25},
    'irradiation': {'min': 1e-10, 'max': 1e+30},
    'experiment': {'min': 1e-30, 'max': 1e+30},
    'simulation_parameter': {'min': 1e-30, 'max': 1e+30},
    'material_property': {'min': 1e-30, 'max': 1e+30},
    'irradiation_condition': {'min': 1e-30, 'max': 1e+30},
    'bubble_characteristics': {'min': 1e-15, 'max': 1e+25},
    'material_processing': {'min': 1e-30, 'max': 1e+30},
    'material_composition': {'min': 0, 'max': 100},
}

# subcategory-level overrides (narrower, more precise)
SUBCATEGORY_RANGES = {
    ('diffusion', 'diffusion_coefficient'): {'min': 1e-30, 'max': 1e-2},
    ('diffusion', 'activation_energy'): {'min': 0.01, 'max': 10.0},
    ('surface_energy', 'surface_energy'): {'min': 0.01, 'max': 10.0},
    ('mechanical', 'elastic_modulus'): {'min': 1e9, 'max': 1e12},
    ('mechanical', 'yield_strength'): {'min': 1e6, 'max': 1e9},
    ('bubble', 'bubble_radius'): {'min': 1e-12, 'max': 1e-3},
    ('bubble', 'bubble_density'): {'min': 1e15, 'max': 1e30},
    ('bubble', 'bubble_pressure'): {'min': 1e3, 'max': 1e12},
    ('thermal', 'thermal_conductivity'): {'min': 0.1, 'max': 500.0},
    ('recrystallization', 'recrystallization_threshold'): {'min': 1e24, 'max': 1e30},
    ('swelling_rate', 'swelling_correlation'): {'min': 1e-30, 'max': 1e+30},
    ('bubble', 'superlattice_spacing'): {'min': 1e-12, 'max': 1e-3},
    ('diffusion', 'general'): {'min': 1e-30, 'max': 1e+30},
    ('bubble', 'general'): {'min': 1e-30, 'max': 1e+30},
    ('rate_theory', 'general'): {'min': 1e-30, 'max': 1e+30},
}

# Skip unit-consistency check for these (too heterogeneous)
UNIT_CHECK_SKIP = {'experiment', 'microstructure', 'irradiation'}
# Also downgrade to INFO for coarse subcategories
UNIT_CHECK_COARSE = {'general', 'swelling_correlation'}

REQUIRED_FIELDS = ['id', 'symbol', 'unit', 'category', 'source_file']
VALUE_TYPES = {'scalar', 'range', 'expression', 'list'}


def load_params(params_dir: Path) -> list[dict]:
    SKIP_PREFIXES = ('_summary', '_comparison', '_conflict', '_all_params', '_validation',
                    '_false_positive', '_improvement', '_paper_mapping', '_match_review')
    records = []
    for f in sorted(params_dir.rglob('*.json')):
        if f.stem.startswith(SKIP_PREFIXES):
            continue
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            records.append({'_file': str(f), '_error': f'JSON parse error: {e}'})
            continue
        items = data if isinstance(data, list) else [data]
        # Handle nested structure: {"parameters": [...]}
        if len(items) == 1 and isinstance(items[0], dict) and 'parameters' in items[0]:
            items = items[0]['parameters']
        for item in items:
            if isinstance(item, dict):
                item.setdefault('_file', str(f))
                records.append(item)
    return records


def check_required_fields(records: list[dict]) -> list[dict]:
    issues = []
    for r in records:
        if '_error' in r:
            continue
        missing = [f for f in REQUIRED_FIELDS if f not in r or not str(r.get(f, '')).strip()]
        vt = r.get('value_type')
        if vt and vt not in VALUE_TYPES:
            missing.append('value_type(invalid)')
        if not vt:
            if 'value' not in r or not str(r.get('value', '')).strip():
                missing.append('value/value_type')
        elif vt == 'scalar' and ('value' not in r or str(r.get('value', '')).strip() == ''):
            missing.append('value')
        elif vt == 'range' and ((r.get('value_min') in (None, '')) or (r.get('value_max') in (None, ''))):
            missing.append('value_min/value_max')
        elif vt == 'expression' and not str(r.get('value_expr', '')).strip():
            missing.append('value_expr')
        elif vt == 'list' and not r.get('values'):
            missing.append('values')
        if missing:
            issues.append({'level': 'fail', 'id': r.get('id', '?'), 'file': r.get('_file', '?'),
                           'check': 'required_fields', 'detail': f'Missing: {missing}'})
    return issues


def check_id_uniqueness(records: list[dict]) -> list[dict]:
    issues, seen = [], {}
    for r in records:
        if '_error' in r:
            continue
        rid = r.get('id', '')
        if rid in seen:
            issues.append({'level': 'fail', 'id': rid, 'file': r.get('_file', '?'),
                           'check': 'id_unique', 'detail': f'Duplicate ID, first in {seen[rid]}'})
        else:
            seen[rid] = r.get('_file', '?')
    return issues


def check_magnitude(records: list[dict]) -> list[dict]:
    issues = []
    for r in records:
        if '_error' in r:
            continue
        cat = r.get('category', '')
        subcat = r.get('subcategory', '')
        rng = SUBCATEGORY_RANGES.get((cat, subcat)) or RANGES.get(cat)
        if not rng:
            continue
        if rng['min'] <= 1e-29 and rng['max'] >= 1e+29:
            continue
        vt = r.get('value_type')
        if vt == 'expression':
            continue
        if vt == 'range' and r.get('value_min') not in (None, '') and r.get('value_max') not in (None, ''):
            vals = [r.get('value_min'), r.get('value_max')]
        elif vt == 'list' and isinstance(r.get('values'), list):
            vals = r.get('values', [])
        else:
            vals = [r.get('value')]
        for raw_val in vals:
            try:
                val = float(raw_val)
            except (ValueError, TypeError):
                issues.append({'level': 'fail', 'id': r.get('id', '?'), 'file': r.get('_file', '?'),
                               'check': 'magnitude', 'detail': f'Non-numeric value: {raw_val}'})
                break
            if val < rng['min'] or val > rng['max']:
                issues.append({'level': 'warn', 'id': r.get('id', '?'), 'file': r.get('_file', '?'),
                               'check': 'magnitude',
                               'detail': f'{val:.4e} outside [{rng["min"]:.0e}, {rng["max"]:.0e}] for {cat}'})
                break
    return issues


def check_unit_consistency(records: list[dict]) -> list[dict]:
    issues = []
    groups = defaultdict(list)
    for r in records:
        if '_error' in r:
            continue
        key = (r.get('category', ''), r.get('subcategory', ''))
        # Skip unit check for heterogeneous categories (broad subcategories)
        if key[0] in UNIT_CHECK_SKIP and (not key[1] or key[1] == 'general'):
            continue
        groups[key].append(r)

    for key, recs in groups.items():
        # Skip coarse subcategories where multiple physical quantities coexist
        if key[1] in UNIT_CHECK_COARSE:
            continue
        units = defaultdict(list)
        for r in recs:
            u = (r.get('unit') or '').strip()
            if u:
                units[u].append(r.get('id', '?'))
        if len(units) > 1:
            top = sorted(units.items(), key=lambda x: -len(x[1]))
            dominant = top[0][0]
            for u, ids in top[1:]:
                issues.append({'level': 'warn', 'id': ids[0], 'file': recs[0].get('_file', '?'),
                               'check': 'unit_consistency',
                               'detail': f'{key}: unit "{u}" ({len(ids)} records) differs from dominant "{dominant}" ({len(top[0][1])} records)'})
    return issues


def check_duplicates(records: list[dict]) -> list[dict]:
    issues, seen = [], {}
    for r in records:
        if '_error' in r:
            continue
        key = (r.get('symbol', ''), r.get('material', ''), str(r.get('temperature', '')))
        if key in seen:
            issues.append({'level': 'warn', 'id': r.get('id', '?'), 'file': r.get('_file', '?'),
                           'check': 'duplicate',
                           'detail': f'Duplicate of {seen[key]} (same symbol+material+temperature)'})
        else:
            seen[key] = r.get('id', '?')
    return issues


def format_console(report: dict) -> str:
    lines = [f"\n{'='*60}", "  Parameter Validation Report", f"{'='*60}\n"]
    lines.append(f"  Files scanned: {report['summary']['files_scanned']}")
    lines.append(f"  Records loaded: {report['summary']['records']}")
    lines.append(f"  Parse errors:   {report['summary']['parse_errors']}\n")

    counts = report['summary']['checks']
    total = sum(v if isinstance(v, int) else v.get('fail',0)+v.get('warn',0)+v.get('pass',0) for v in counts.values())
    lines.append(f"  {'Check':<22} {'PASS':>6} {'WARN':>6} {'FAIL':>6}")
    lines.append(f"  {'-'*22} {'-'*6} {'-'*6} {'-'*6}")
    for check, c in counts.items():
        if isinstance(c, int):
            continue
        lines.append(f"  {check:<22} {c.get('pass',0):>6} {c.get('warn',0):>6} {c.get('fail',0):>6}")
    lines.append(f"  {'-'*22} {'-'*6} {'-'*6} {'-'*6}")
    lines.append(f"  {'TOTAL':<22} {counts.get('_pass',0):>6} {counts.get('_warn',0):>6} {counts.get('_fail',0):>6}")

    if report['issues']:
        lines.append(f"\n  Issues ({len(report['issues'])}):\n")
        for i, iss in enumerate(report['issues'], 1):
            lines.append(f"  {i:>3}. [{iss['level'].upper()}] {iss['check']}: {iss['id']} in {iss['file']}")
            lines.append(f"       {iss['detail']}")
    else:
        lines.append("\n  ✅ All checks passed!")

    return '\n'.join(lines)


def format_markdown(report: dict) -> str:
    lines = ["# Parameter Validation Report\n"]
    s = report['summary']
    lines.append(f"- **Files scanned:** {s['files_scanned']}")
    lines.append(f"- **Records loaded:** {s['records']}")
    lines.append(f"- **Parse errors:** {s['parse_errors']}\n")

    counts = s['checks']
    lines.append("| Check | PASS | WARN | FAIL |")
    lines.append("|-------|------|------|------|")
    for check, c in counts.items():
        if check.startswith('_'):
            continue
        lines.append(f"| {check} | {c.get('pass',0)} | {c.get('warn',0)} | {c.get('fail',0)} |")
    lines.append(f"| **TOTAL** | **{counts.get('_pass',0)}** | **{counts.get('_warn',0)}** | **{counts.get('_fail',0)}** |\n")

    if report['issues']:
        lines.append("## Issues\n")
        for i, iss in enumerate(report['issues'], 1):
            badge = '🔴' if iss['level'] == 'fail' else '🟡'
            lines.append(f"{i}. {badge} **{iss['check']}** — `{iss['id']}` in `{iss['file']}`")
            lines.append(f"   > {iss['detail']}\n")
    else:
        lines.append("✅ All checks passed!")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Validate material parameter JSON files')
    parser.add_argument('params_dir', type=Path, help='Directory containing JSON parameter files')
    parser.add_argument('--json-output', type=Path, help='Write JSON report to file')
    parser.add_argument('--markdown-output', type=Path, help='Write Markdown report to file')
    args = parser.parse_args()

    if not args.params_dir.is_dir():
        print(f"Error: {args.params_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    records = load_params(args.params_dir)
    valid_records = [r for r in records if '_error' not in r]
    parse_errors = len(records) - len(valid_records)

    check_fns = [
        ('required_fields', check_required_fields),
        ('id_unique', check_id_uniqueness),
        ('magnitude', check_magnitude),
        ('unit_consistency', check_unit_consistency),
        ('duplicate', check_duplicates),
    ]

    all_issues = []
    counts = {}
    total_p, total_w, total_f = 0, 0, 0

    for name, fn in check_fns:
        issues = fn(records)
        p = len(valid_records) - len(issues)
        w = sum(1 for i in issues if i['level'] == 'warn')
        f = sum(1 for i in issues if i['level'] == 'fail')
        counts[name] = {'pass': p, 'warn': w, 'fail': f}
        total_p += p; total_w += w; total_f += f
        all_issues.extend(issues)

    counts['_pass'] = total_p
    counts['_warn'] = total_w
    counts['_fail'] = total_f

    report = {
        'summary': {
            'files_scanned': len(list(args.params_dir.rglob('*.json'))),
            'records': len(valid_records),
            'parse_errors': parse_errors,
            'checks': counts,
        },
        'issues': all_issues,
    }

    print(format_console(report))

    if args.json_output:
        args.json_output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"\nJSON report → {args.json_output}")

    if args.markdown_output:
        args.markdown_output.write_text(format_markdown(report), encoding='utf-8')
        print(f"Markdown report → {args.markdown_output}")

    sys.exit(1 if total_f > 0 else 0)


if __name__ == '__main__':
    main()
