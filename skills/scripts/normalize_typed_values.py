#!/usr/bin/env python3
"""Normalize parameter values into typed schema.

Adds:
- value_type: scalar|range|expression
- value_min/value_max for ranges
- value_expr for unparsed expressions

Safe migration: preserves original `value`.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

SKIP_PREFIXES = ('_summary', '_comparison', '_conflict', '_all_params', '_validation',
                 '_false_positive', '_improvement', '_paper_mapping', '_match_review')
NUM = r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
RANGE_PATTERNS = [
    re.compile(rf'^\s*({NUM})\s*(?:to|–|—|-)\s*({NUM})\s*$'),
]


def parse_typed_value(v):
    if isinstance(v, (int, float)):
        return {'value_type': 'scalar', 'value': v}
    if not isinstance(v, str):
        return {'value_type': 'expression', 'value_expr': str(v)}
    s = v.strip()
    try:
        return {'value_type': 'scalar', 'value': float(s)}
    except Exception:
        pass
    for pat in RANGE_PATTERNS:
        m = pat.match(s)
        if m:
            a, b = float(m.group(1)), float(m.group(2))
            lo, hi = (a, b) if a <= b else (b, a)
            return {'value_type': 'range', 'value_min': lo, 'value_max': hi, 'value': s}
    return {'value_type': 'expression', 'value_expr': s, 'value': s}


def get_records(raw):
    if isinstance(raw, dict) and 'parameters' in raw and isinstance(raw['parameters'], list):
        return raw['parameters']
    if isinstance(raw, list):
        return raw
    return None


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    changed_files = changed_records = 0
    for f in sorted(root.rglob('*.json')):
        if f.stem.startswith(SKIP_PREFIXES):
            continue
        try:
            raw = json.loads(f.read_text(encoding='utf-8'))
        except Exception:
            continue
        records = get_records(raw)
        if not records:
            continue
        changed = False
        for r in records:
            if not isinstance(r, dict):
                continue
            if 'value_type' in r:
                continue
            parsed = parse_typed_value(r.get('value'))
            r.update(parsed)
            changed = True
            changed_records += 1
        if changed:
            f.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding='utf-8')
            changed_files += 1
    print(json.dumps({'changed_files': changed_files, 'changed_records': changed_records}, ensure_ascii=False))

if __name__ == '__main__':
    main()
