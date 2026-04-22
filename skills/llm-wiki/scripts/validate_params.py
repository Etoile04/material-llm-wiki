#!/usr/bin/env python3
"""Validate extracted material parameter JSON files for quality issues."""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

# ─── Unit-to-SI conversion table ───────────────────────────────────────────────
# Maps a unit string to (si_base_unit, factor) so that si_value = raw_value * factor.
UNIT_TO_SI = {
    # Pressure
    'Pa':  ('Pa',  1.0),
    'kPa': ('Pa',  1e3),
    'MPa': ('Pa',  1e6),
    'GPa': ('Pa',  1e9),
    # Length
    'm':   ('m',   1.0),
    'mm':  ('m',   1e-3),
    'μm':  ('m',   1e-6),
    'um':  ('m',   1e-6),
    'nm':  ('m',   1e-9),
    # Energy
    'J':   ('J',   1.0),
    'kJ':  ('J',   1e3),
    'eV':  ('J',   1.602e-19),
    # Temperature (no conversion, just pass through)
    'K':   ('K',   1.0),
    '°C':  ('K',   1.0),
    # Time
    's':   ('s',   1.0),
    'ms':  ('s',   1e-3),
    'μs':  ('s',   1e-6),
    'us':  ('s',   1e-6),
    'ns':  ('s',   1e-9),
    # Diffusivity
    'm²/s':   ('m²/s',   1.0),
    'cm²/s':  ('m²/s',   1e-4),
    'mm²/s':  ('m²/s',   1e-6),
    # Density
    'g/cm³':  ('kg/m³',  1e3),
    'kg/m³':  ('kg/m³',  1.0),
    # Dimensionless
    'dimensionless': ('dimensionless', 1.0),
    '%':             ('dimensionless', 0.01),
    # Misc
    'K⁻¹':  ('K⁻¹',  1.0),
    'fissions/m³': ('fissions/m³', 1.0),
    'fissions/nm³': ('fissions/m³', 1e27),
    'dpa':  ('dpa', 1.0),
    'W/m·K': ('W/m·K', 1.0),
    'W/(m·K)': ('W/m·K', 1.0),
    'J/mol': ('J/mol', 1.0),
    'kJ/mol': ('J/mol', 1e3),
    'eV/atom': ('J', 1.602e-19),
    'at.%': ('dimensionless', 0.01),
    'wt.%': ('dimensionless', 0.01),
}

# ─── RANGES (all in SI base units) ─────────────────────────────────────────────
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
    'simulation': {'min': 1e-30, 'max': 1e+30},
    'simulation_parameter': {'min': 1e-30, 'max': 1e+30},
    'material_property': {'min': 1e-30, 'max': 1e+30},
    'irradiation_condition': {'min': 1e-30, 'max': 1e+30},
    'bubble_characteristics': {'min': 1e-15, 'max': 1e+25},
    'material_processing': {'min': 1e-30, 'max': 1e+30},
    'material_composition': {'min': 0, 'max': 100},
    'elastic': {'min': 1e9, 'max': 1e12},
    'thermodynamic': {'min': 1e-30, 'max': 1e+30},
    'physical': {'min': 1e-30, 'max': 1e+30},
    'phase_transformation': {'min': 1e-30, 'max': 1e+30},
    'crystal_structure': {'min': 1e-30, 'max': 1e+30},
}

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
    ('elastic', 'elastic_modulus'): {'min': 1e9, 'max': 1e12},
    ('elastic', 'shear_modulus'): {'min': 1e9, 'max': 1e12},
    ('elastic', 'bulk_modulus'): {'min': 1e9, 'max': 1e12},
}

# Skip unit-consistency check for these (too heterogeneous)
UNIT_CHECK_SKIP = {'experiment', 'microstructure', 'irradiation'}
UNIT_CHECK_COARSE = {'general', 'swelling_correlation'}

REQUIRED_FIELDS = ['id', 'symbol', 'unit', 'category', 'source_file']
VALUE_TYPES = {'scalar', 'range', 'expression', 'list'}


def to_si(value: float, unit: str) -> tuple[float, str] | None:
    """Convert value to SI base units. Returns (si_value, si_unit) or None if unrecognized."""
    u = unit.strip()
    if u in UNIT_TO_SI:
        si_unit, factor = UNIT_TO_SI[u]
        return (value * factor, si_unit)
    # Try normalizing unicode variants
    u_norm = u.replace('²', '2').replace('³', '3').replace('μ', 'u').replace('·', '*')
    if u_norm in UNIT_TO_SI:
        si_unit, factor = UNIT_TO_SI[u_norm]
        return (value * factor, si_unit)
    return None


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
        elif vt == 'scalar' and ('value' not in r or str(r.get('value', '')) == ''):
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


def _extract_numeric_values(r: dict) -> list[float] | None:
    """Extract numeric values from a record. Returns None if no values to check."""
    vt = r.get('value_type')
    if vt == 'expression':
        return None
    if vt == 'range' and r.get('value_min') not in (None, '') and r.get('value_max') not in (None, ''):
        return [r.get('value_min'), r.get('value_max')]
    elif vt == 'list' and isinstance(r.get('values'), list):
        vals = []
        for item in r.get('values', []):
            if isinstance(item, dict):
                for v in item.values():
                    if isinstance(v, (int, float)):
                        vals.append(float(v))
                    elif isinstance(v, str):
                        try:
                            vals.append(float(v))
                        except (ValueError, TypeError):
                            pass
            elif isinstance(item, (int, float)):
                vals.append(float(item))
            elif isinstance(item, str):
                try:
                    vals.append(float(item))
                except (ValueError, TypeError):
                    pass
        return vals if vals else None
    else:
        return [r.get('value')]


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

        vals = _extract_numeric_values(r)
        if vals is None:
            continue

        unit = (r.get('unit') or '').strip()

        # Try to convert to SI base units
        for raw_val in vals:
            try:
                val = float(raw_val)
            except (ValueError, TypeError):
                issues.append({'level': 'fail', 'id': r.get('id', '?'), 'file': r.get('_file', '?'),
                               'check': 'magnitude', 'detail': f'Non-numeric value: {raw_val}'})
                break

            result = to_si(val, unit)
            if result is not None:
                si_val, si_unit = result
                check_val = si_val
            else:
                # Unrecognized unit — downgrade to warn only
                check_val = val
                si_unit = unit

            if check_val < rng['min'] or check_val > rng['max']:
                if result is None:
                    level = 'warn'
                    detail = f'{val:.4e} {unit} outside [{rng["min"]:.0e}, {rng["max"]:.0e}] for {cat} (unrecognized unit, SI conversion skipped)'
                else:
                    level = 'warn'
                    detail = f'{val:.4e} {unit} → {check_val:.4e} {si_unit} outside [{rng["min"]:.0e}, {rng["max"]:.0e}] for {cat}'
                issues.append({'level': level, 'id': r.get('id', '?'), 'file': r.get('_file', '?'),
                               'check': 'magnitude', 'detail': detail})
                break
    return issues


def check_unit_consistency(records: list[dict]) -> list[dict]:
    issues = []
    groups = defaultdict(list)
    for r in records:
        if '_error' in r:
            continue
        key = (r.get('category', ''), r.get('subcategory', ''))
        if key[0] in UNIT_CHECK_SKIP and (not key[1] or key[1] == 'general'):
            continue
        groups[key].append(r)

    for key, recs in groups.items():
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
                # Skip if units are convertible to same SI base
                dominant_si = to_si(1.0, dominant)
                other_si = to_si(1.0, u)
                if dominant_si and other_si and dominant_si[1] == other_si[1]:
                    continue
                issues.append({'level': 'warn', 'id': ids[0], 'file': recs[0].get('_file', '?'),
                               'check': 'unit_consistency',
                               'detail': f'{key}: unit "{u}" ({len(ids)} records) differs from dominant "{dominant}" ({len(top[0][1])} records)'})
    return issues


def check_duplicates(records: list[dict]) -> list[dict]:
    issues, seen = [], {}
    for r in records:
        if '_error' in r:
            continue
        key = (
            r.get('symbol', ''),
            r.get('material', ''),
            str(r.get('temperature', '')),
            r.get('method', ''),
            r.get('region', ''),
        )
        if key in seen:
            issues.append({'level': 'warn', 'id': r.get('id', '?'), 'file': r.get('_file', '?'),
                           'check': 'duplicate',
                           'detail': f'Duplicate of {seen[key]} (same symbol+material+temperature+method+region)'})
        else:
            seen[key] = r.get('id', '?')
    return issues


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
        if len(items) == 1 and isinstance(items[0], dict) and 'parameters' in items[0]:
            items = items[0]['parameters']
        for item in items:
            if isinstance(item, dict):
                item.setdefault('_file', str(f))
                records.append(item)
    return records


def format_console(report: dict) -> str:
    lines = [f"\n{'='*60}", "  Parameter Validation Report", f"{'='*60}\n"]
    lines.append(f"  Files scanned: {report['summary']['files_scanned']}")
    lines.append(f"  Records loaded: {report['summary']['records']}")
    lines.append(f"  Parse errors:   {report['summary']['parse_errors']}\n")

    counts = report['summary']['checks']
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
