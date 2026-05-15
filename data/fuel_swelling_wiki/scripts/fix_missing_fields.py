#!/usr/bin/env python3
"""Auto-fix script for parameter JSON records missing required fields.

Fixes missing value_type, name, category, and source_file by applying
deterministic inference rules.
"""

import glob
import json
import os
import sys


def infer_value_type(record: dict) -> str:
    """Infer value_type from the value field's Python type."""
    # If already set, keep it
    if record.get("value_type"):
        return record["value_type"]

    val = record.get("value")

    if val is None:
        return "scalar"

    if isinstance(val, bool):
        return "scalar"

    if isinstance(val, (int, float)):
        return "scalar"

    if isinstance(val, list):
        return "list"

    if isinstance(val, dict):
        # Check for range keys
        range_keys = {"min", "max", "low", "high"}
        if range_keys & set(val.keys()):
            return "range"
        return "scalar"

    if isinstance(val, str):
        # Check for LaTeX expressions
        latex_markers = ["$", "\\frac", "\\exp", "\\sqrt", "\\times"]
        if any(marker in val for marker in latex_markers):
            return "expression"
        return "scalar"

    return "scalar"


def infer_name(record: dict) -> str:
    """Infer name from property (priority 1), description (priority 2), or fallback."""
    if record.get("name"):
        return record["name"]

    if record.get("property"):
        return record["property"]

    if record.get("description"):
        return record["description"]

    return "未命名参数"


def infer_category(record: dict) -> str:
    """Return existing category or 'uncategorized'."""
    if record.get("category"):
        return record["category"]
    return "uncategorized"


def infer_source_file(record: dict, filename: str) -> None:
    """Set source_file from filename if missing. Mutates record in place."""
    if not record.get("source_file"):
        # Strip .json extension
        name = filename
        if name.endswith(".json"):
            name = name[:-5]
        record["source_file"] = name


def fix_record(record: dict, filename: str) -> tuple:
    """Fix one record, returning (fixed_record, list_of_changed_field_names)."""
    changed = []

    # value_type
    if not record.get("value_type"):
        inferred = infer_value_type(record)
        record["value_type"] = inferred
        changed.append("value_type")

    # name
    if not record.get("name"):
        inferred = infer_name(record)
        record["name"] = inferred
        changed.append("name")

    # category
    if not record.get("category"):
        record["category"] = infer_category(record)
        changed.append("category")

    # source_file
    if not record.get("source_file"):
        infer_source_file(record, filename)
        changed.append("source_file")

    return record, changed


def fix_file(filepath: str) -> tuple:
    """Fix all records in a JSON file. Returns (total_records, fixed_count).

    Only writes back if changes were made.
    """
    filename = os.path.basename(filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        records = json.load(f)

    if not isinstance(records, list):
        print(f"  WARNING: {filename} is not a list — skipped", file=sys.stderr)
        return 0, 0

    total = len(records)
    fixed_count = 0
    any_changed = False

    for i, record in enumerate(records):
        _, changed = fix_record(record, filename)
        if changed:
            fixed_count += 1
            any_changed = True

    if any_changed:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

    return total, fixed_count


def main():
    """Scan all .json files in ../parameters/ and run fixes."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    params_dir = os.path.join(script_dir, "..", "parameters")

    pattern = os.path.join(params_dir, "*.json")
    files = sorted(glob.glob(pattern))

    if not files:
        print("No JSON files found in", params_dir)
        return

    total_files = 0
    total_records = 0
    total_fixed = 0

    for filepath in files:
        rec_count, fixed_count = fix_file(filepath)
        total_files += 1
        total_records += rec_count
        total_fixed += fixed_count
        if fixed_count > 0:
            print(f"  Fixed {fixed_count}/{rec_count} records in {os.path.basename(filepath)}")

    print(f"\nSummary: {total_files} files, {total_records} records, {total_fixed} fixed")


if __name__ == "__main__":
    main()
