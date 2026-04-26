#!/usr/bin/env python3
"""Scaffold a new LLM Wiki knowledge base."""

import sys
import os
from datetime import datetime
from pathlib import Path


def scaffold(wiki_root: str, topic: str):
    root = Path(wiki_root)
    today = datetime.now().strftime("%Y%m%d")
    date_display = datetime.now().strftime("%Y-%m-%d")

    # Create directory structure
    dirs = [
        "log",
        "audit/resolved",
        "raw/articles",
        "raw/papers",
        "raw/refs",
        "wiki/concepts",
        "wiki/entities",
        "wiki/summaries",
        "parameters",
        "outputs/queries",
    ]
    for d in dirs:
        (root / d).mkdir(parents=True, exist_ok=True)

    # CLAUDE.md
    claude_md = root / "CLAUDE.md"
    if not claude_md.exists():
        claude_md.write_text(f"""# {topic} — Schema

## ⚡ Pre-Action Checks (MANDATORY — read before ANY write)

```
提取参数前: python3 scripts/batch_extract.py --mode find-underextracted
提取参数后: python3 scripts/batch_extract.py --mode post-validate
新论文入库: pipeline/ingest_single_full.lobster → check registry first
```

**禁止**: 直接 sessions_spawn 手写 prompt 提取参数
**禁止**: 不查 paper_registry.json 就创建新 slug
**禁止**: 提取后不运行 post-validate (issues 必须 = 0)

---

## Scope

This wiki covers {topic}.

## Naming Conventions

- **Summaries**: `YYYY_FirstAuthor_ShortTitle.md`
- **Concepts**: `ConceptName.md` (PascalCase)
- **Entities**: `EntityName.md`
- **Parameters**: `<source_slug>.json`

## Terminology

(Define domain-specific terms here)

## Units

- Temperature: K or °C (specify)
- Swelling: % (specify linear or volumetric)

## 防重复规则 ⚠️ MANDATORY

**写入任何 summary 或 parameter 文件前，必须检查 `paper_registry.json`！**

1. **DOI 查重**: 有 DOI → 搜索 registry → 已存在则追加，禁止创建新 slug
2. **标题模糊匹配**: 无 DOI → title similarity > 0.85 匹配
3. **Author+Year 查重**: 用 first_author + year 组合检查
4. **Slug 格式**: 必须为 `YYYY_FirstAuthor_ShortTitle`，年份在前
5. **注册新论文**: 写入后必须注册到 `paper_registry.json`
6. **报告/手册**: 无 DOI 用 `report_id` 字段代替

## Current Articles

### Concepts (0)
(none yet)

### Entities (0)
(none yet)

### Summaries (0)
(none yet)

## Research Gaps

1. (List topics needing more sources)

## Open Questions

1. (List unresolved issues)

## Recent Activity

- {date_display}: Wiki scaffolded
""")

    # paper_registry.json (empty)
    registry = root / "paper_registry.json"
    if not registry.exists():
        registry.write_text("{}")
        print(f"   paper_registry.json: {registry}")

    # wiki/index.md
    index_md = root / "wiki" / "index.md"
    if not index_md.exists():
        index_md.write_text(f"""# Index — {topic}

> {topic}

## 🔖 Navigation
- [[#Concepts]] · [[#Entities]] · [[#Summaries]] · [[#Open Questions]]

## Concepts

(none yet)

## Entities

(none yet)

## Summaries (chronological)

(none yet)

## Open Questions

(none yet)
""")

    # log file
    log_file = root / "log" / f"{today}.md"
    if not log_file.exists():
        log_file.write_text(f"""# {date_display}

## [{datetime.now().strftime('%H:%M')}] scaffold | Created wiki for "{topic}"
""")

    print(f"✅ Wiki scaffolded at: {root}")
    print(f"   CLAUDE.md: {claude_md}")
    print(f"   wiki/index.md: {index_md}")
    print(f"   log: {log_file}")
    print()
    print("Next steps:")
    print("  1. Fill in CLAUDE.md — scope, conventions, gaps")
    print("  2. Copy sources to raw/ or create refs/ pointers")
    print("  3. Tell agent: 'ingest raw/papers/first-paper.md'")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scaffold.py <wiki-root> '<Topic Title>'")
        sys.exit(1)
    scaffold(sys.argv[1], sys.argv[2])
