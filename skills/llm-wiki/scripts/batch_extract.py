#!/usr/bin/env python3
"""
Batch deep extraction with built-in dedup, schema validation, and registry check.

Usage:
    python batch_extract.py --wiki-root /path/to/wiki --papers slug1 slug2 ...
    python batch_extract.py --wiki-root /path/to/wiki --from-raw-unextracted
    python batch_extract.py --wiki-root /path/to/wiki --from-raw-underextracted --threshold 40

This script does NOT call the LLM itself. It:
1. Identifies candidate papers (unextracted or under-extracted)
2. Checks paper_registry.json for duplicates
3. Generates standardized sub-agent prompts
4. Outputs a ready-to-run task list for sessions_spawn

After sub-agents complete, run:
    python batch_extract.py --wiki-root /path/to/wiki --post-validate
"""

import json
import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict


# ============================================================
# Schema & Validation
# ============================================================

VALID_VALUE_TYPES = {"scalar", "range", "expression", "list"}
VALID_CATEGORIES = {
    "thermodynamic", "thermal", "mechanical", "diffusion", "irradiation",
    "bubble", "swelling", "phase_transformation", "microstructure", "creep",
    "fission_product", "fuel_performance", "corrosion", "elastic", "other",
    "crystal_structure", "physical", "surface_energy", "simulation",
}
VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_METHODS = {
    "experimental", "DFT", "MD", "phase-field", "rate_theory", "CALPHAD",
    "analytical", "empirical", "compilation", "review", "XRD", "TEM", "SEM",
    "APT", "neutron_diffraction", "dilatometry", "calorimetry",
}
REQUIRED_FIELDS = {"id", "name", "symbol", "unit", "category", "source_file", "confidence"}


def validate_param(p: dict) -> list[str]:
    """Validate a single parameter against schema. Returns list of issues."""
    issues = []

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in p or not p.get(field):
            issues.append(f"missing required field: {field}")

    # value_type
    vt = p.get("value_type", "")
    if vt and vt not in VALID_VALUE_TYPES:
        issues.append(f"invalid value_type: {vt!r} (allowed: {VALID_VALUE_TYPES})")

    # Check for common wrong field names
    if "scalar" in p and "value" not in p:
        issues.append("uses 'scalar' instead of 'value'")
    if "number" in p and "value" not in p:
        issues.append("uses 'number' instead of 'value'")

    # value_type specific
    if vt == "scalar" and "value" not in p:
        issues.append("scalar type missing 'value' field")
    elif vt == "range" and ("value_min" not in p or "value_max" not in p):
        issues.append("range type missing 'value_min' or 'value_max'")
    elif vt == "expression" and "value_expr" not in p:
        issues.append("expression type missing 'value_expr'")

    # category
    cat = p.get("category", "")
    if cat and cat not in VALID_CATEGORIES:
        issues.append(f"invalid category: {cat!r}")

    # confidence
    conf = p.get("confidence", "")
    if conf and conf not in VALID_CONFIDENCE:
        issues.append(f"invalid confidence: {conf!r}")

    # Slug format in id: should be YYYY_Author
    pid = p.get("id", "")
    if pid and not re.match(r'\d{4}_', pid):
        issues.append(f"id doesn't start with YYYY_: {pid[:30]}")

    return issues


def validate_file(path: str) -> dict:
    """Validate a parameter JSON file. Returns report."""
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict) and "parameters" in data:
        return {"error": "nested dict format (should be plain array)", "params": []}

    if not isinstance(data, list):
        return {"error": f"unexpected format: {type(data).__name__}", "params": []}

    issues_by_param = {}
    id_set = set()
    duplicates = []

    for i, p in enumerate(data):
        param_issues = validate_param(p)
        if param_issues:
            issues_by_param[i] = param_issues

        pid = p.get("id", "")
        if pid in id_set:
            duplicates.append(pid)
        id_set.add(pid)

    return {
        "total": len(data),
        "issues": issues_by_param,
        "duplicate_ids": duplicates,
        "params": data,
    }


# ============================================================
# Registry & Duplicate Detection
# ============================================================

def load_registry(wiki_root: Path) -> dict:
    """Load paper_registry.json."""
    path = wiki_root / "paper_registry.json"
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_registry(wiki_root: Path, registry: dict):
    """Save paper_registry.json."""
    path = wiki_root / "paper_registry.json"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def check_duplicate(doi: str, title: str, year: str, author: str, registry: dict) -> str | None:
    """Check if a paper already exists in registry. Returns existing slug or None."""
    # DOI exact match
    if doi:
        for key, entry in registry.items():
            if entry.get("doi") == doi:
                return entry["slug"]

    # Title fuzzy match (simple: check if key words overlap > 80%)
    if title:
        title_words = set(re.findall(r'[a-zA-Z]{4,}', title.lower()))
        if len(title_words) > 3:
            for key, entry in registry.items():
                entry_title = entry.get("title", "")
                entry_words = set(re.findall(r'[a-zA-Z]{4,}', entry_title.lower()))
                if not entry_words:
                    continue
                overlap = len(title_words & entry_words) / min(len(title_words), len(entry_words))
                if overlap > 0.80:
                    return entry["slug"]

    # Author + Year match
    if year and author:
        for key, entry in registry.items():
            if str(entry.get("year")) == str(year) and entry.get("first_author", "").lower() == author.lower():
                return entry["slug"]

    return None


# ============================================================
# Slug Standardization
# ============================================================

def standardize_slug(slug: str) -> str:
    """Ensure slug follows YYYY_FirstAuthor_ShortTitle format."""
    # Already starts with year
    if re.match(r'^\d{4}_', slug):
        return slug

    # Try to extract year and rearrange
    year_match = re.search(r'(19\d{2}|20\d{2})', slug)
    if year_match:
        year = year_match.group(1)
        # Remove year from current position and prepend
        rest = slug.replace(year, "", 1).strip("_")
        return f"{year}_{rest}"

    return slug


# ============================================================
# Raw Dir → Slug Matching
# ============================================================

def match_raw_to_slug(raw_dir_name: str, param_slugs: set[str]) -> str | None:
    """Try to match a raw MD directory name to an existing parameter slug."""
    years = set(re.findall(r'(19\d{2}|20\d{2})', raw_dir_name))
    authors = set(w.lower() for w in re.findall(r'[A-Z][a-z]{2,}', raw_dir_name))

    best_slug = None
    best_score = 0

    for slug in param_slugs:
        slug_years = set(re.findall(r'(19\d{2}|20\d{2})', slug))
        slug_authors = set(w.lower() for w in re.findall(r'[A-Z][a-z]{2,}', slug))

        year_overlap = len(years & slug_years)
        author_overlap = len(authors & slug_authors)
        score = year_overlap * 10 + author_overlap * 5

        if score > best_score and score >= 10:
            best_score = score
            best_slug = slug

    return best_slug


# ============================================================
# Prompt Generation
# ============================================================

EXTRACTION_PROMPT_TEMPLATE = """你是核材料知识库的参数提取专家。请从文献的原始 MD 文本中深度提取所有可量化的参数。

## ⚠️ 防重复规则（MANDATORY）
1. 读取现有参数 JSON 文件（如果存在）
2. 只追加不重复的参数（通过 id 去重）
3. 不要创建新 slug，追加到现有文件
4. 如果是新论文，slug 必须为 `{slug}`

## 提取规则（必须遵守）
1. JSON 输出纯数组 `[...]`，不要嵌套在对象里
2. 数值必须存在 `value` 字段（禁止 scalar/number 等其他字段名）
3. `value_type` 只允许: scalar | range | expression | list
4. 没有具体数值的参数不要创建记录
5. 定性参数用 `value_type: expression`，描述文本存在 `value_expr`
6. 表格中的数值要全部提取，每个单元格一条记录
7. 公式中的系数、常数要单独提取

## Schema
```json
{{"id":"{slug}_简短描述","name":"中文名","symbol":"$LaTeX$","value_type":"scalar","unit":"单位","category":"thermodynamic|thermal|mechanical|diffusion|irradiation|bubble|swelling|phase_transformation|microstructure|creep|fission_product|fuel_performance|corrosion|elastic|other","material":"材料","source_paper":"{source_paper}","confidence":"high|medium|low","description":"来源(Table/Eq编号)","method":"experimental|DFT|MD|phase-field|rate_theory|CALPHAD|analytical|empirical|compilation|review","value":数值,"source_file":"{source_file}"}}
```

## 文献信息
- Raw: {raw_path}
- 参数文件: {param_path}
- 现有参数数: {existing_count}

## 工作流程
1. 用 read 工具读取 raw MD 文件
2. 用 read 工具读取现有参数 JSON（如存在）
3. 从 raw MD 提取所有新的可量化参数
4. 用 write 工具写入合并后的 JSON
5. 报告新增参数数量和类别分布"""


def generate_prompt(slug: str, raw_path: str, param_path: str, existing_count: int) -> str:
    """Generate standardized extraction prompt."""
    source_paper = slug.split("_")[1] + "_" + slug.split("_")[0] if "_" in slug else slug
    return EXTRACTION_PROMPT_TEMPLATE.format(
        slug=slug,
        raw_path=raw_path,
        param_path=param_path,
        existing_count=existing_count,
        source_paper=source_paper,
        source_file=f"raw/mineru/{slug}/paper.md",
    )


# ============================================================
# Main Commands
# ============================================================

def cmd_find_candidates(wiki_root: Path, mode: str, threshold: int = 40) -> list[dict]:
    """Find papers that need extraction."""
    raw_dir = wiki_root / "raw" / "mineru"
    params_dir = wiki_root / "parameters"
    registry = load_registry(wiki_root)

    # Get existing param slugs and counts
    param_info = {}
    for f in os.listdir(params_dir):
        if not f.endswith('.json'):
            continue
        slug = f.replace('.json', '')
        with open(params_dir / f, encoding='utf-8') as fp:
            data = json.load(fp)
            n = len(data) if isinstance(data, list) else 0
        param_info[slug] = n

    candidates = []

    for rd in sorted(os.listdir(raw_dir)):
        rd_path = raw_dir / rd
        if not os.path.isdir(rd_path):
            continue

        # Find MD file
        mds = [f for f in os.listdir(rd_path) if f.endswith('.md')]
        if not mds:
            continue
        md_path = os.path.join(rd_path, mds[0])
        md_size = os.path.getsize(md_path)

        if md_size < 5000:  # Skip tiny files
            continue

        # Try to match to existing slug
        matched_slug = match_raw_to_slug(rd, set(param_info.keys()))

        if matched_slug:
            existing_count = param_info.get(matched_slug, 0)

            if mode == "unextracted":
                continue  # Already has params

            if mode == "underextracted" and existing_count >= threshold:
                continue  # Already well-extracted

            slug = matched_slug
            param_path = str(params_dir / f"{matched_slug}.json")
        else:
            # Truly new paper — generate slug from raw dir
            year_match = re.search(r'(19\d{2}|20\d{2})', rd)
            if not year_match:
                continue  # Can't determine year

            # Check registry for duplicate
            dup = check_duplicate("", rd, year_match.group(1), "", registry)
            if dup:
                slug = dup
                param_path = str(params_dir / f"{dup}.json")
                existing_count = param_info.get(dup, 0)
            else:
                # Generate a slug
                slug = standardize_slug(rd.replace(" ", "_")[:60])
                param_path = str(params_dir / f"{slug}.json")
                existing_count = 0

        candidates.append({
            "slug": slug,
            "raw_path": md_path,
            "param_path": param_path,
            "existing_count": existing_count,
            "raw_size": md_size,
        })

    return candidates


def cmd_post_validate(wiki_root: Path):
    """Validate all parameter files after extraction."""
    params_dir = wiki_root / "parameters"
    total_issues = 0
    total_params = 0
    files_with_issues = []

    for f in sorted(os.listdir(params_dir)):
        if not f.endswith('.json'):
            continue
        path = params_dir / f
        result = validate_file(str(path))

        total_params += result["total"]
        issue_count = len(result.get("issues", {})) + len(result.get("duplicate_ids", []))

        if result.get("error"):
            print(f"❌ {f}: {result['error']}")
            files_with_issues.append(f)
            total_issues += 1
        elif issue_count > 0:
            print(f"⚠️  {f}: {result['total']} params, {issue_count} issues")
            # Show first 3 issues
            for idx, issues in list(result["issues"].items())[:3]:
                print(f"    param[{idx}]: {', '.join(issues)}")
            if result.get("duplicate_ids"):
                print(f"    duplicate IDs: {result['duplicate_ids'][:5]}")
            files_with_issues.append(f)
            total_issues += issue_count
        else:
            print(f"✅ {f}: {result['total']} params")

    print(f"\n{'='*60}")
    print(f"Total: {total_params} params in {len(os.listdir(params_dir))} files")
    print(f"Files with issues: {len(files_with_issues)}")
    print(f"Total issues: {total_issues}")


def cmd_generate_tasks(wiki_root: Path, candidates: list[dict], group_size: int = 6):
    """Generate sub-agent task descriptions grouped for parallel execution."""
    groups = [candidates[i:i+group_size] for i in range(0, len(candidates), group_size)]

    print(f"Generated {len(groups)} groups ({len(candidates)} papers total)")
    print(f"Copy each group's prompt to sessions_spawn\n")

    for gi, group in enumerate(groups):
        print(f"{'='*60}")
        print(f"Group {gi+1} ({len(group)} papers)")
        print(f"{'='*60}")

        # Build combined prompt
        paper_list = []
        for p in group:
            prompt = generate_prompt(
                p["slug"], p["raw_path"], p["param_path"], p["existing_count"]
            )
            paper_list.append(f"### 论文: {p['slug']} ({p['existing_count']} existing, {p['raw_size']//1024}KB raw)\n- Raw: {p['raw_path']}\n- Params: {p['param_path']}\n")

        header = f"你是核材料知识库的参数提取专家。请从以下 {len(group)} 篇文献中深度提取参数。\n\n"
        header += "## 规则\n1. JSON 纯数组 `[...]` 2. value 字段存数值 3. value_type: scalar|range|expression|list 4. 无数值不创建 5. 表格每格一条\n\n"

        for pl in paper_list:
            header += pl + "\n"

        print(header[:500] + "...\n")

    # Also output as JSON for programmatic use
    tasks_path = wiki_root / "scripts" / "_extraction_tasks.json"
    with open(tasks_path, 'w', encoding='utf-8') as f:
        json.dump({"groups": groups, "total_papers": len(candidates)}, f, indent=2, ensure_ascii=False)
    print(f"\nTask list saved to: {tasks_path}")


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Batch extraction with dedup & validation")
    parser.add_argument("--wiki-root", required=True, help="Wiki root directory")
    parser.add_argument("--mode", choices=["find-unextracted", "find-underextracted", "post-validate", "generate-tasks"],
                       default="find-underextracted", help="Operation mode")
    parser.add_argument("--threshold", type=int, default=40, help="Param count threshold for 'underextracted'")
    parser.add_argument("--group-size", type=int, default=6, help="Papers per sub-agent group")

    args = parser.parse_args()
    wiki_root = Path(args.wiki_root)

    if args.mode == "post-validate":
        cmd_post_validate(wiki_root)
        return

    mode = "underextracted" if args.mode == "find-underextracted" else "unextracted"
    if args.mode == "generate-tasks":
        # Combine both
        candidates_under = cmd_find_candidates(wiki_root, "underextracted", args.threshold)
        candidates_new = cmd_find_candidates(wiki_root, "unextracted")
        candidates = candidates_new + candidates_under
        cmd_generate_tasks(wiki_root, candidates, args.group_size)
        return

    candidates = cmd_find_candidates(wiki_root, mode, args.threshold)

    print(f"Found {len(candidates)} candidates ({mode}, threshold={args.threshold}):\n")
    for c in sorted(candidates, key=lambda x: -x['raw_size']):
        print(f"  {c['existing_count']:>3} params  {c['raw_size']:>7}B  {c['slug']}")


if __name__ == "__main__":
    main()
