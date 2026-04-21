#!/usr/bin/env python3
"""compare_params.py — 参数比对脚本 v2

比对 v1 和 v2 两个目录下的 JSON 参数文件，生成差异报告。

用法:
    python3 compare_params.py <v1_dir> <v2_dir> [--json-output report.json] [--markdown-output report.md]
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

# ── 常见单位换算因子 ──────────────────────────────────────────
UNIT_FACTORS = {
    frozenset({"m²/s", "cm²/s"}): 1e4,
    frozenset({"m²/s", "mm²/s"}): 1e6,
    frozenset({"cm²/s", "mm²/s"}): 100,
    frozenset({"w/m·k", "w/cm·k"}): 100,
    frozenset({"g/cm³", "kg/m³"}): 1e3,
    frozenset({"mpa", "gpa"}): 1e3,
    frozenset({"j/mol·k", "j/mol"}): 1,  # same value, just name difference
}


def load_json(filepath: str) -> list | dict | None:
    """容错加载 JSON"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"[WARN] 跳过 {filepath}: {e}", file=sys.stderr)
        return None


def load_all_jsons(directory: str) -> dict[str, list]:
    """加载目录下所有 JSON，返回 {filename: data}，兼容 list / {data:[...]} / {parameters:[...]}"""
    result = {}
    skip_prefixes = ('_summary', '_comparison', '_conflict', '_all_params', '_validation',
                     '_false_positive', '_improvement', '_paper_mapping', '_match_review', '_phaseB_report')
    for f in sorted(os.listdir(directory)):
        if not f.endswith('.json') or Path(f).stem.startswith(skip_prefixes):
            continue
        data = load_json(os.path.join(directory, f))
        if isinstance(data, list):
            result[f] = data
        elif isinstance(data, dict) and 'data' in data and isinstance(data['data'], list):
            result[f] = data['data']
        elif isinstance(data, dict) and 'parameters' in data and isinstance(data['parameters'], list):
            result[f] = data['parameters']
    return result


# ── 论文名解析 ────────────────────────────────────────────────

def parse_v1_filename(name: str) -> dict:
    """解析 v1: YYYY_FirstAuthor_ShortTitle.json"""
    stem = Path(name).stem
    parts = stem.split("_", 2)
    return {
        "year": parts[0] if len(parts) > 0 else "",
        "author": parts[1].lower() if len(parts) > 1 else "",
        "keywords": [w.lower() for w in parts[2:]] if len(parts) > 2 else [],
        "raw": stem,
    }


def parse_v2_filename(name: str) -> dict:
    """解析 v2: first_author_YEAR_*  或  151846_*  等"""
    stem = Path(name).stem
    parts = stem.split("_")

    # pattern: firstauthor_YEAR_xxx
    if len(parts) >= 2 and parts[1].isdigit() and len(parts[1]) == 4:
        return {
            "year": parts[1],
            "author": parts[0].lower(),
            "keywords": [w.lower() for w in parts[2:]],
            "raw": stem,
        }

    # pattern: 151846_xxx
    if len(parts) >= 1 and parts[0].isdigit():
        return {
            "year": "",
            "author": "",
            "keywords": [w.lower() for w in parts[1:]],
            "raw": stem,
        }

    # fallback: try to find a 4-digit year anywhere
    year = ""
    for p in parts:
        if p.isdigit() and len(p) == 4 and 1900 <= int(p) <= 2030:
            year = p
            break
    return {
        "year": year,
        "author": parts[0].lower() if parts else "",
        "keywords": [w.lower() for w in parts if w != year] if year else [w.lower() for w in parts],
        "raw": stem,
    }


def filename_similarity(a: dict, b: dict) -> float:
    """计算两个解析后的文件名相似度 [0, 1]"""
    score = 0.0

    # year match
    if a["year"] and b["year"]:
        score += 0.4 if a["year"] == b["year"] else 0.0

    # author match
    if a["author"] and b["author"]:
        score += 0.3 * SequenceMatcher(None, a["author"], b["author"]).ratio()

    # keyword overlap
    if a["keywords"] and b["keywords"]:
        overlap = sum(1 for ka in a["keywords"] for kb in b["keywords"]
                      if ka in kb or kb in ka)
        total = max(len(a["keywords"]), len(b["keywords"]), 1)
        score += 0.3 * (overlap / total)

    return score


def load_explicit_mapping(mapping_path: str | None) -> list[tuple[str, str, float]]:
    if not mapping_path or not os.path.exists(mapping_path):
        return []
    data = load_json(mapping_path)
    if not isinstance(data, dict):
        return []
    out = []
    for item in data.get('mappings', []):
        if not isinstance(item, dict):
            continue
        v1 = item.get('v1')
        v2 = item.get('v2')
        if v1 and v2:
            out.append((f'{v1}.json' if not str(v1).endswith('.json') else v1,
                        f'{v2}.json' if not str(v2).endswith('.json') else v2,
                        float(item.get('confidence', 1.0))))
    return out


def map_v1_to_v2(v1_files: dict, v2_files: dict, explicit_mappings: list[tuple[str, str, float]] | None = None) -> list[tuple[str, str, float]]:
    """建立 v1→v2 论文映射，返回 [(v1_file, v2_file, score)]"""
    mappings = []
    used_v1, used_v2 = set(), set()
    for v1f, v2f, score in (explicit_mappings or []):
        if v1f in v1_files and v2f in v2_files:
            mappings.append((v1f, v2f, score))
            used_v1.add(v1f)
            used_v2.add(v2f)

    parsed_v1 = {f: parse_v1_filename(f) for f in v1_files if f not in used_v1}
    parsed_v2 = {f: parse_v2_filename(f) for f in v2_files if f not in used_v2}

    candidates = []
    for v1f, p1 in parsed_v1.items():
        for v2f, p2 in parsed_v2.items():
            s = filename_similarity(p1, p2)
            if s > 0.3:
                candidates.append((s, v1f, v2f))
    candidates.sort(reverse=True)

    for score, v1f, v2f in candidates:
        if v1f in used_v1 or v2f in used_v2:
            continue
        mappings.append((v1f, v2f, score))
        used_v1.add(v1f)
        used_v2.add(v2f)

    return mappings


# ── 记录匹配 ──────────────────────────────────────────────────

def normalize(s: str) -> str:
    if not s:
        return ""
    return s.replace("$", "").strip().lower()


def get_field(rec: dict, key: str) -> str:
    """从 record 取字段，兼容多种 key 风格"""
    if not rec:
        return ""
    for k in (key, key.replace("_", " "), key.replace("_", "-")):
        if k in rec and rec[k]:
            return str(rec[k]).strip()
    # case-insensitive fallback
    rec_lower = {str(k).lower(): str(v) for k, v in rec.items()}
    if key.lower() in rec_lower:
        return rec_lower[key.lower()].strip()
    return ""


def record_key(rec: dict) -> str:
    """生成匹配键: symbol + name_en + material + temperature_range"""
    parts = [
        normalize(get_field(rec, "symbol")),
        normalize(get_field(rec, "name_en")),
        normalize(get_field(rec, "material")),
        normalize(get_field(rec, "temperature_range")),
    ]
    return "|".join(parts)


def get_value(rec: dict) -> str:
    """获取主值字段，兼容 typed value schema"""
    vt = get_field(rec, 'value_type')
    if vt == 'range':
        vmin = get_field(rec, 'value_min')
        vmax = get_field(rec, 'value_max')
        if vmin and vmax:
            return f'{vmin} to {vmax}'
    elif vt == 'expression':
        expr = get_field(rec, 'value_expr')
        if expr:
            return expr
    elif vt == 'list':
        vals = rec.get('values')
        if isinstance(vals, list):
            return ', '.join(str(x) for x in vals)
    for k in ('value', 'param_value', 'numerical_value'):
        v = get_field(rec, k)
        if v:
            return v
    return ''


def get_unit(rec: dict) -> str:
    for k in ("unit", "param_unit"):
        v = get_field(rec, k)
        if v:
            return normalize(v)
    return ""


def temp_ranges_overlap(t1: str, t2: str) -> bool:
    """检查两个温度范围是否有重叠"""
    def parse_range(s):
        nums = re.findall(r"[-+]?\d*\.?\d+", s.replace(",", " "))
        return [float(x) for x in nums]

    r1, r2 = parse_range(t1), parse_range(t2)
    if not r1 or not r2:
        return True  # 无法解析则认为匹配
    lo1, hi1 = min(r1), max(r1)
    lo2, hi2 = min(r2), max(r2)
    return lo1 <= hi2 and lo2 <= hi1


def records_match(r1: dict, r2: dict) -> bool:
    """判断两条记录是否匹配"""
    if normalize(get_field(r1, "symbol")) != normalize(get_field(r2, "symbol")):
        return False
    if normalize(get_field(r1, "name_en")) != normalize(get_field(r2, "name_en")):
        return False
    if normalize(get_field(r1, "material")) != normalize(get_field(r2, "material")):
        return False
    if not temp_ranges_overlap(get_field(r1, "temperature_range"),
                                get_field(r2, "temperature_range")):
        return False
    return True


# ── 差异分类 ──────────────────────────────────────────────────

def _parse_scalarish(v: str):
    s = str(v).replace(',', '').replace('~', '').strip()
    try:
        return ('scalar', float(s))
    except Exception:
        pass
    m = re.match(r'^\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s*(?:to|–|—|-)\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s*$', str(v).strip())
    if m:
        a, b = float(m.group(1)), float(m.group(2))
        return ('range', (min(a,b), max(a,b)))
    return (None, None)


def classify_diff(v1_val: str, v2_val: str, v1_unit: str, v2_unit: str) -> dict:
    """分类差异，返回 {category, description, ratio}"""
    t1, p1 = _parse_scalarish(v1_val)
    t2, p2 = _parse_scalarish(v2_val)
    if not t1 or not t2:
        return {"category": "无法比较", "description": f"非数值/表达式: v1={v1_val}, v2={v2_val}", "ratio": None}
    if t1 == 'range' and t2 == 'range':
        lo1, hi1 = p1; lo2, hi2 = p2
        if abs(lo1-lo2) < 1e-12 and abs(hi1-hi2) < 1e-12:
            return {"category": "相同", "description": "范围一致", "ratio": 0}
        overlap = (lo1 <= hi2 and lo2 <= hi1)
        if overlap:
            return {"category": "小幅修正", "description": f"范围有重叠: [{lo1}, {hi1}] vs [{lo2}, {hi2}]", "ratio": None}
        return {"category": "大幅修正", "description": f"范围不重叠: [{lo1}, {hi1}] vs [{lo2}, {hi2}]", "ratio": None}
    f1 = p1[0] if t1 == 'range' else p1
    f2 = p2[0] if t2 == 'range' else p2

    if f1 == 0 and f2 == 0:
        return {"category": "相同", "description": "值均为 0", "ratio": 0}

    if f1 == 0:
        return {"category": "大幅修正", "description": f"v1=0, v2={f2}", "ratio": float("inf")}

    abs_diff = abs(f1 - f2)
    rel_diff = abs_diff / abs(f1)

    # check unit conversion
    if v1_unit and v2_unit:
        for pair, factor in UNIT_FACTORS.items():
            if v1_unit in pair and v2_unit in pair:
                expected_ratio = factor if abs(f2) > abs(f1) else 1.0 / factor
                actual_ratio = abs(f2 / f1)
                if abs(actual_ratio / expected_ratio - 1) < 0.05:
                    return {
                        "category": "单位换算",
                        "description": f"{v1_unit} → {v2_unit} (×{factor})",
                        "ratio": rel_diff,
                    }

    if rel_diff < 1e-10:
        return {"category": "相同", "description": "值一致", "ratio": rel_diff}
    elif rel_diff <= 0.01:
        return {"category": "相同", "description": f"差异极小 ({rel_diff:.2%})", "ratio": rel_diff}
    elif rel_diff <= 0.5:
        return {"category": "小幅修正", "description": f"差异 {rel_diff:.2%} (可能是精度提升)", "ratio": rel_diff}
    elif rel_diff <= 10:
        return {"category": "大幅修正", "description": f"差异 {rel_diff:.2%}", "ratio": rel_diff}
    else:
        return {"category": "⚠️ 疑似匹配错误", "description": f"差异 {rel_diff:.2%}，需人工审核", "ratio": rel_diff}


# ── 比对核心 ──────────────────────────────────────────────────

def compare_records(v1_recs: list, v2_recs: list, v1_file: str, v2_file: str) -> list[dict]:
    """比对两组记录，返回差异列表"""
    results = []
    matched_v2 = set()

    for i, r1 in enumerate(v1_recs):
        best_j = -1
        for j, r2 in enumerate(v2_recs):
            if j in matched_v2:
                continue
            if records_match(r1, r2):
                best_j = j
                break

        if best_j >= 0:
            matched_v2.add(best_j)
            r2 = v2_recs[best_j]
            v1_val = get_value(r1)
            v2_val = get_value(r2)
            v1_unit = get_unit(r1)
            v2_unit = get_unit(r2)
            diff = classify_diff(v1_val, v2_val, v1_unit, v2_unit)

            results.append({
                "type": "matched",
                "category": diff["category"],
                "v1_file": v1_file,
                "v2_file": v2_file,
                "v1_index": i,
                "v2_index": best_j,
                "symbol": get_field(r1, "symbol"),
                "name_en": get_field(r1, "name_en"),
                "material": get_field(r1, "material"),
                "temperature_range": get_field(r1, "temperature_range"),
                "v1_value": v1_val,
                "v1_unit": v1_unit,
                "v2_value": v2_val,
                "v2_unit": v2_unit,
                "diff_ratio": diff["ratio"],
                "description": diff["description"],
            })
        else:
            results.append({
                "type": "missing_in_v2",
                "v1_file": v1_file,
                "v1_index": i,
                "symbol": get_field(r1, "symbol"),
                "name_en": get_field(r1, "name_en"),
                "material": get_field(r1, "material"),
                "v1_value": get_value(r1),
                "v1_unit": get_unit(r1),
            })

    for j, r2 in enumerate(v2_recs):
        if j not in matched_v2:
            results.append({
                "type": "new_in_v2",
                "v2_file": v2_file,
                "v2_index": j,
                "symbol": get_field(r2, "symbol"),
                "name_en": get_field(r2, "name_en"),
                "material": get_field(r2, "material"),
                "v2_value": get_value(r2),
                "v2_unit": get_unit(r2),
            })

    return results


def run_comparison(v1_dir: str, v2_dir: str, mapping_path: str | None = None) -> dict:
    """运行完整比对，返回报告 dict"""
    v1_files = load_all_jsons(v1_dir)
    v2_files = load_all_jsons(v2_dir)
    explicit = load_explicit_mapping(mapping_path)
    mappings = map_v1_to_v2(v1_files, v2_files, explicit)

    all_results = []
    mapped_v1 = set()
    mapped_v2 = set()

    for v1f, v2f, score in mappings:
        mapped_v1.add(v1f)
        mapped_v2.add(v2f)
        recs = compare_records(v1_files[v1f], v2_files[v2f], v1f, v2f)
        all_results.extend(recs)

    # unmapped v1
    for v1f in v1_files:
        if v1f not in mapped_v1:
            for i, r1 in enumerate(v1_files[v1f]):
                all_results.append({
                    "type": "unmapped_v1",
                    "v1_file": v1f,
                    "v1_index": i,
                    "symbol": get_field(r1, "symbol"),
                    "name_en": get_field(r1, "name_en"),
                    "material": get_field(r1, "material"),
                    "v1_value": get_value(r1),
                    "v1_unit": get_unit(r1),
                })

    # unmapped v2
    for v2f in v2_files:
        if v2f not in mapped_v2:
            for i, r2 in enumerate(v2_files[v2f]):
                all_results.append({
                    "type": "unmapped_v2",
                    "v2_file": v2f,
                    "v2_index": i,
                    "symbol": get_field(r2, "symbol"),
                    "name_en": get_field(r2, "name_en"),
                    "material": get_field(r2, "material"),
                    "v2_value": get_value(r2),
                    "v2_unit": get_unit(r2),
                })

    # stats
    matched = [r for r in all_results if r["type"] == "matched"]
    same = [r for r in matched if r["category"] == "相同"]
    unit_conv = [r for r in matched if r["category"] == "单位换算"]
    minor = [r for r in matched if r["category"] == "小幅修正"]
    major = [r for r in matched if r["category"] == "大幅修正"]
    errors = [r for r in matched if "疑似" in r["category"]]
    missing = [r for r in all_results if r["type"] in ("missing_in_v2", "unmapped_v1")]
    new = [r for r in all_results if r["type"] in ("new_in_v2", "unmapped_v2")]

    return {
        "summary": {
            "v1_files": len(v1_files),
            "v2_files": len(v2_files),
            "mapped_papers": len(mappings),
            "total_matched": len(matched),
            "same": len(same),
            "unit_conversion": len(unit_conv),
            "minor_correction": len(minor),
            "major_correction": len(major),
            "suspected_errors": len(errors),
            "missing_in_v2": len(missing),
            "new_in_v2": len(new),
        },
        "paper_mappings": [{"v1_file": m[0], "v2_file": m[1], "score": round(m[2], 3)} for m in mappings],
        "details": all_results,
    }


# ── 报告输出 ──────────────────────────────────────────────────

def render_markdown(report: dict) -> str:
    s = report["summary"]
    lines = [
        "# 参数比对报告\n",
        "## 📊 统计摘要\n",
        f"| 项目 | 数量 |",
        f"|------|------|",
        f"| v1 文件数 | {s['v1_files']} |",
        f"| v2 文件数 | {s['v2_files']} |",
        f"| 成功映射论文 | {s['mapped_papers']} |",
        f"| 参数匹配总数 | {s['total_matched']} |",
        f"| ✅ 相同 | {s['same']} |",
        f"| 🔄 单位换算 | {s['unit_conversion']} |",
        f"| 📝 小幅修正 | {s['minor_correction']} |",
        f"| ⚠️ 大幅修正 | {s['major_correction']} |",
        f"| ❌ 疑似匹配错误 | {s['suspected_errors']} |",
        f"| 📭 v2 中缺失 | {s['missing_in_v2']} |",
        f"| 🆕 v2 中新增 | {s['new_in_v2']} |",
        "\n---\n",
    ]

    # paper mappings
    lines.append("## 📑 论文映射\n")
    for m in report["paper_mappings"]:
        lines.append(f"- `{m['v1_file']}` → `{m['v2_file']}` (相似度: {m['score']})")
    lines.append("")

    # errors first
    errors = [d for d in report["details"] if "疑似" in d.get("category", "")]
    if errors:
        lines.append("## ❌ 疑似匹配错误（需人工审核）\n")
        for e in errors:
            lines.append(f"### {e.get('symbol', '?')} — {e.get('name_en', '?')}\n")
            lines.append(f"- **材料**: {e.get('material', '?')}")
            lines.append(f"- **温度范围**: {e.get('temperature_range', '?')}")
            lines.append(f"- **v1**: `{e.get('v1_value', '?')}` {e.get('v1_unit', '')} (文件: `{e.get('v1_file', '?')}` #{e.get('v1_index', '?')})")
            lines.append(f"- **v2**: `{e.get('v2_value', '?')}` {e.get('v2_unit', '')} (文件: `{e.get('v2_file', '?')}` #{e.get('v2_index', '?')})")
            lines.append(f"- **差异**: {e.get('description', '?')}\n")

    # major corrections
    major = [d for d in report["details"] if d.get("category") == "大幅修正"]
    if major:
        lines.append("## ⚠️ 大幅修正\n")
        for e in major:
            lines.append(f"- **{e.get('symbol', '?')}** {e.get('name_en', '?')} | {e.get('material', '?')}")
            lines.append(f"  v1: `{e.get('v1_value', '?')}` → v2: `{e.get('v2_value', '?')}` ({e.get('description', '?')})")
        lines.append("")

    # minor
    minor = [d for d in report["details"] if d.get("category") == "小幅修正"]
    if minor:
        lines.append("## 📝 小幅修正\n")
        for e in minor:
            lines.append(f"- **{e.get('symbol', '?')}** {e.get('name_en', '?')} | {e.get('material', '?')}")
            lines.append(f"  v1: `{e.get('v1_value', '?')}` → v2: `{e.get('v2_value', '?')}` ({e.get('description', '?')})")
        lines.append("")

    # unit conversions
    conv = [d for d in report["details"] if d.get("category") == "单位换算"]
    if conv:
        lines.append("## 🔄 单位换算\n")
        for e in conv:
            lines.append(f"- **{e.get('symbol', '?')}** {e.get('name_en', '?')} | {e.get('description', '?')}")
            lines.append(f"  v1: `{e.get('v1_value', '?')}` {e.get('v1_unit', '')} → v2: `{e.get('v2_value', '?')}` {e.get('v2_unit', '')}")
        lines.append("")

    # missing
    missing = [d for d in report["details"] if d["type"] in ("missing_in_v2", "unmapped_v1")]
    if missing:
        lines.append("## 📭 v2 中缺失\n")
        for e in missing:
            f = e.get("v1_file", "?")
            lines.append(f"- **{e.get('symbol', '?')}** {e.get('name_en', '?')} | `{e.get('v1_value', '?')}` {e.get('v1_unit', '')} ({f})")
        lines.append("")

    # new
    new = [d for d in report["details"] if d["type"] in ("new_in_v2", "unmapped_v2")]
    if new:
        lines.append("## 🆕 v2 中新增\n")
        for e in new:
            f = e.get("v2_file", "?")
            lines.append(f"- **{e.get('symbol', '?')}** {e.get('name_en', '?')} | `{e.get('v2_value', '?')}` {e.get('v2_unit', '')} ({f})")
        lines.append("")

    return "\n".join(lines)


# ── main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="参数比对工具 v2")
    parser.add_argument("v1_dir", help="v1 版本 JSON 目录")
    parser.add_argument("v2_dir", help="v2 版本 JSON 目录")
    parser.add_argument("--mapping", help="显式论文映射 JSON 路径")
    parser.add_argument("--json-output", "-j", help="JSON 报告输出路径")
    parser.add_argument("--markdown-output", "-m", help="Markdown 报告输出路径")
    args = parser.parse_args()

    if not os.path.isdir(args.v1_dir):
        print(f"[ERROR] 目录不存在: {args.v1_dir}", file=sys.stderr)
        sys.exit(1)
    if not os.path.isdir(args.v2_dir):
        print(f"[ERROR] 目录不存在: {args.v2_dir}", file=sys.stderr)
        sys.exit(1)

    report = run_comparison(args.v1_dir, args.v2_dir, args.mapping)

    if args.json_output:
        with open(args.json_output, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"[OK] JSON 报告: {args.json_output}")

    if args.markdown_output:
        md = render_markdown(report)
        with open(args.markdown_output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"[OK] Markdown 报告: {args.markdown_output}")
    else:
        print(render_markdown(report))

    # exit code
    s = report["summary"]
    if s["suspected_errors"] > 0:
        print(f"\n[!] 发现 {s['suspected_errors']} 个疑似匹配错误，请人工审核", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
