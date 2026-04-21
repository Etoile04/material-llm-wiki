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
