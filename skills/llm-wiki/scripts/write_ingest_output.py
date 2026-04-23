#!/usr/bin/env python3
"""Write ingest output files (summary + params) to wiki."""
import argparse, json, os, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--params", required=True)
    parser.add_argument("--wiki-root", required=True)
    args = parser.parse_args()

    # Write summary
    sum_dir = os.path.join(args.wiki_root, "wiki", "summaries")
    os.makedirs(sum_dir, exist_ok=True)
    sum_path = os.path.join(sum_dir, f"{args.slug}.md")
    
    # Parse summary - it's JSON with summary_markdown field
    try:
        summary_data = json.loads(args.summary)
        md_content = summary_data.get("summary_markdown", args.summary)
    except json.JSONDecodeError:
        md_content = args.summary
    
    with open(sum_path, "w") as f:
        f.write(md_content)
    print(f"Wrote summary: {sum_path}")

    # Write parameters
    param_dir = os.path.join(args.wiki_root, "parameters")
    os.makedirs(param_dir, exist_ok=True)
    param_path = os.path.join(param_dir, f"{args.slug}.json")
    
    try:
        params_data = json.loads(args.params)
        if isinstance(params_data, list):
            params = params_data
        else:
            params = params_data.get("parameters", [])
    except json.JSONDecodeError:
        params = []
    
    with open(param_path, "w") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)
    print(f"Wrote params: {param_path} ({len(params)} params)")

if __name__ == "__main__":
    main()
