#!/usr/bin/env python3
"""
Post-ingest verification gate.
Checks that expected outputs (summary + params) actually exist for each slug.
Run after every batch to catch silent subagent failures.
"""
import json
import os
import sys
from pathlib import Path

# Import slug sanitizer from skills
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'skills', 'llm-wiki', 'scripts'))
from slug_utils import sanitize_slug


def verify_slugs(wiki_root: Path, slugs: list) -> dict:
    """Verify that all slugs have both summary and params files."""
    summaries_dir = wiki_root / "wiki" / "summaries"
    params_dir = wiki_root / "parameters"
    
    results = {"ok": [], "missing_summary": [], "missing_params": [],
               "empty_summary": [], "empty_params": [], "bad_json": []}
    
    for slug in slugs:
        safe_slug = sanitize_slug(slug)
        
        # Check summary - try safe slug first, then raw
        summ_found = False
        for candidate in [safe_slug, slug]:
            summ_path = summaries_dir / f"{candidate}.md"
            if summ_path.exists():
                if summ_path.stat().st_size < 100:
                    results["empty_summary"].append(slug)
                summ_found = True
                break
        if not summ_found:
            results["missing_summary"].append(slug)
        
        # Check params - try safe slug first, then raw
        param_found = False
        for candidate in [safe_slug, slug]:
            param_path = params_dir / f"{candidate}.json"
            if param_path.exists():
                if param_path.stat().st_size < 10:
                    results["empty_params"].append(slug)
                    param_found = True
                    break
                try:
                    data = json.load(open(param_path))
                    if not isinstance(data, list) or len(data) == 0:
                        results["bad_json"].append(f"{slug} (not array or empty)")
                except json.JSONDecodeError as e:
                    results["bad_json"].append(f"{slug} ({e})")
                param_found = True
                break
        if not param_found:
            results["missing_params"].append(slug)
    
    ok_count = len(slugs) - len(set(results["missing_summary"] + results["missing_params"] + 
                                      results["empty_summary"] + results["empty_params"] + 
                                      [s.split(" (")[0] for s in results["bad_json"]]))
    results["ok_count"] = ok_count
    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Verify ingest outputs")
    parser.add_argument("--wiki-root", required=True)
    parser.add_argument("--slugs", nargs="+", help="Slugs to verify")
    parser.add_argument("--from-file", help="File with one slug per line")
    args = parser.parse_args()
    
    wiki_root = Path(args.wiki_root)
    slugs = args.slugs or []
    
    if args.from_file:
        with open(args.from_file) as f:
            slugs.extend(line.strip() for line in f if line.strip())
    
    if not slugs:
        print("No slugs to verify")
        return
    
    report = verify_slugs(wiki_root, slugs)
    
    print(f"Verified {len(slugs)} slugs:")
    print(f"  OK: {report['ok_count']}")
    
    for issue_type in ["missing_summary", "missing_params", "empty_summary", "empty_params", "bad_json"]:
        if report[issue_type]:
            print(f"  X {issue_type}: {len(report[issue_type])}")
            for s in report[issue_type][:10]:
                print(f"      {s}")
            if len(report[issue_type]) > 10:
                print(f"      ... and {len(report[issue_type])-10} more")
    
    total_issues = sum(len(report[k]) for k in ["missing_summary", "missing_params", "empty_summary", "empty_params", "bad_json"])
    sys.exit(1 if total_issues > 0 else 0)


if __name__ == "__main__":
    main()
