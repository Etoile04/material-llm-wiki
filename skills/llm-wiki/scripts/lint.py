#!/usr/bin/env python3
"""Lint an LLM Wiki — check health of the knowledge base."""

import re
import sys
import os
from pathlib import Path
from datetime import datetime, timedelta


def find_wikilinks(text: str) -> list[str]:
    """Extract [[wikilinks]] from text."""
    return re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]', text)


def lint_wiki(wiki_root: str):
    root = Path(wiki_root)
    issues = []

    wiki_dir = root / "wiki"
    if not wiki_dir.exists():
        print("❌ No wiki/ directory found")
        return

    # Collect all wiki pages
    wiki_pages = set()
    for md in wiki_dir.rglob("*.md"):
        rel = md.relative_to(root).with_suffix("")
        wiki_pages.add(str(rel))
        # Also add just the filename (short form)
        wiki_pages.add(md.stem)

    # 1. Check dead wikilinks
    for md in wiki_dir.rglob("*.md"):
        content = md.read_text(encoding="utf-8", errors="ignore")
        links = find_wikilinks(content)
        for link in links:
            # Skip anchor-only links (page-internal) and empty links
            if not link.strip() or link.strip().startswith('#'):
                continue
            # Check if target exists
            target_path = wiki_dir / f"{link}.md"
            target_rel = root / f"{link}.md"
            if not target_path.exists() and not target_rel.exists() and link not in wiki_pages:
                rel = md.relative_to(root)
                issues.append(f"DEAD_LINK: {rel} → [[{link}]]")

    # 2. Check orphan pages (no inbound links)
    all_links_incoming = set()
    for md in wiki_dir.rglob("*.md"):
        content = md.read_text(encoding="utf-8", errors="ignore")
        links = find_wikilinks(content)
        for link in links:
            all_links_incoming.add(link)
            all_links_incoming.add(md.stem)

    for md in wiki_dir.rglob("*.md"):
        if md.name == "index.md":
            continue
        stem = md.stem
        if stem not in all_links_incoming:
            rel = md.relative_to(root)
            issues.append(f"ORPHAN: {rel} (no inbound links)")

    # 3. Check oversized pages
    for md in wiki_dir.rglob("*.md"):
        content = md.read_text(encoding="utf-8", errors="ignore")
        words = len(content.split())
        if words > 1500:
            rel = md.relative_to(root)
            issues.append(f"OVERSIZED: {rel} ({words} words, limit 1500)")

    # 4. Check wiki/index.md exists and is non-empty
    index = wiki_dir / "index.md"
    if not index.exists():
        issues.append("MISSING: wiki/index.md")
    else:
        content = index.read_text(encoding="utf-8", errors="ignore")
        if len(content) < 100:
            issues.append("STUB: wiki/index.md is nearly empty")

    # 5. Check CLAUDE.md
    claude = root / "CLAUDE.md"
    if not claude.exists():
        issues.append("MISSING: CLAUDE.md")
    else:
        content = claude.read_text(encoding="utf-8", errors="ignore")
        if "Scope" not in content:
            issues.append("INCOMPLETE: CLAUDE.md missing Scope section")

    # 6. Check log/
    log_dir = root / "log"
    if not log_dir.exists() or not any(log_dir.glob("*.md")):
        issues.append("MISSING: log/ directory or empty")

    # 7. Check open audits
    audit_dir = root / "audit"
    open_audits = []
    if audit_dir.exists():
        for f in audit_dir.glob("*.md"):
            open_audits.append(f.name)
        if open_audits:
            issues.append(f"AUDITS: {len(open_audits)} open audit(s) pending")

    # 8. Check for KaTeX usage (positive signal)
    katex_count = 0
    for md in wiki_dir.rglob("*.md"):
        content = md.read_text(encoding="utf-8", errors="ignore")
        katex_count += len(re.findall(r'\$[^$]+\$', content))
    
    # 9. Check for mermaid usage (positive signal)
    mermaid_count = 0
    for md in wiki_dir.rglob("*.md"):
        content = md.read_text(encoding="utf-8", errors="ignore")
        mermaid_count += len(re.findall(r'```mermaid', content))

    # Report
    print(f"=== LLM Wiki Lint: {root} ===\n")
    
    wiki_count = sum(1 for _ in wiki_dir.rglob("*.md"))
    summaries = sum(1 for _ in (wiki_dir / "summaries").glob("*.md")) if (wiki_dir / "summaries").exists() else 0
    concepts = sum(1 for _ in (wiki_dir / "concepts").rglob("*.md")) if (wiki_dir / "concepts").exists() else 0
    entities = sum(1 for _ in (wiki_dir / "entities").glob("*.md")) if (wiki_dir / "entities").exists() else 0
    params = sum(1 for _ in (root / "parameters").glob("*.json")) if (root / "parameters").exists() else 0

    print(f"📊 Stats:")
    print(f"   Wiki pages: {wiki_count}")
    print(f"   Summaries: {summaries}")
    print(f"   Concepts: {concepts}")
    print(f"   Entities: {entities}")
    print(f"   Parameters: {params} files")
    print(f"   KaTeX formulas: {katex_count}")
    print(f"   Mermaid diagrams: {mermaid_count}")
    print(f"   Open audits: {len(open_audits)}")
    print()

    if issues:
        print(f"⚠️  Issues ({len(issues)}):")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("✅ No issues found!")

    return issues


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lint.py <wiki-root>")
        sys.exit(1)
    issues = lint_wiki(sys.argv[1])
    sys.exit(len(issues))
