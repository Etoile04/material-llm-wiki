#!/usr/bin/env python3
"""
Zotero → LLM Wiki Auto-Sync
Detects new/updated items in Zotero collections and prepares them for ingest.

Usage:
  python3 zotero_sync.py --mode detect [--collection UMo|UZr|all] [--output /tmp/sync_result.json]
  python3 zotero_sync.py --mode convert --input /tmp/sync_result.json
  python3 zotero_sync.py --mode status
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────
ZOTERO_API = "http://localhost:23119/api/users/0"
WIKI_ROOT = os.environ.get("WIKI_ROOT", "data/fuel_swelling_wiki")
REGISTRY_PATH = os.path.join(WIKI_ROOT, "paper_registry.json")
SYNC_STATE_PATH = os.path.join(WIKI_ROOT, "zotero_sync_state.json")

# Collection tree definitions (key → display name)
COLLECTION_TREE = {
    "UMo": {
        "root": "IZ3U245C",
        "name": "U-Mo 燃料",
        "subcollections": [
            "ELI8NGWD",  # UMo dispersed
            "LWL8I4QJ",  # UMo Monolithic
            "6QSDHSVG",  # experimental
            "9AIZ7TQS",  # irradiation
            "WUKSAYKA",  # APT
            "U86EYKRT",  # ion irradiation
            "ZGIDXF56",  # manufacture
            "2KDRUFIK",  # phase transformation
            "Z828WF7B",  # FCCI
            "FYFSXVN3",  # general
            "HMYCAY56",  # modeling
            "U5ZA85UX",  # 辐照扩散系数
            "JZMXJ694",  # 相场模拟
            "7JKMH2HH",  # Defects
            "5KH6UPPN",  # Interatomic Potential
            "RLUW5S2V",  # irradiation thermodynamics
            "BS77JDGR",  # multi-elements phase transition
            "E2H3W3MH",  # swelling
            "S9VBW9WG",  # thermo-mechanics
            "NUNQ79SE",  # superlattice
            "T7DB3DP9",  # AKMC
            "MNGK7KJT",  # Experimental
            "GUD7QDH2",  # PF
            "2T73THTH",  # review
            "U2ANVMBU",  # UMo-Al
            "JE79A9LW",  # UMoSi
        ],
    },
    "UZr": {
        "root": "XVYWG8MR",
        "name": "U-Zr 燃料",
        "subcollections": [
            "4E3Z2A4X", "89D6XZQM", "8IAFBQGP", "AKPW7HMW",
            "DIYJHFUL", "FYGIF4ZS", "GMECAV63", "HYR2TUXC",
            "MSZ5NCIJ", "MVJHLMCL", "PYBGR4JD", "TLKGXJRI",
            "WK6ELFNN", "WMPVHIML", "ZP53EY4H",
        ],
    },
}


# ── Zotero API helpers ──────────────────────────────────────────────

def api_get(path, **params):
    """GET from Zotero local API."""
    qs = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{ZOTERO_API}{path}?{qs}" if qs else f"{ZOTERO_API}{path}"
    try:
        resp = urllib.request.urlopen(url, timeout=30)
        return json.loads(resp.read())
    except Exception as e:
        print(f"API error: {url} → {e}", file=sys.stderr)
        return []


def get_collection_items(col_keys):
    """Get all non-attachment items from a list of collection keys."""
    all_items = {}
    for ck in col_keys:
        start = 0
        while True:
            items = api_get(
                f"/collections/{ck}/items",
                format="json", limit="100", start=str(start),
                **{"itemType": "-attachment"},
            )
            for i in items:
                d = i["data"]
                if d.get("itemType") not in ("attachment", "note", "annotation"):
                    all_items[d["key"]] = d
            if len(items) < 100:
                break
            start += 100
            time.sleep(0.02)
    return all_items


def get_pdf_path(item_key):
    """Find PDF attachment path for an item."""
    children = api_get(f"/items/{item_key}/children", format="json")
    for child in children:
        d = child["data"]
        if d.get("contentType") == "application/pdf" and d.get("linkMode", "").startswith("imported"):
            filename = d.get("filename", "")
            return f"/Users/lwj04/Zotero/storage/{item_key}/{filename}" if filename else None
    # Check child attachments (sometimes PDF is a child of a child)
    for child in children:
        d = child["data"]
        if d.get("itemType") == "attachment" and d.get("contentType") != "application/pdf":
            grand_children = api_get(f"/items/{d['key']}/children", format="json")
            for gc in grand_children:
                gd = gc["data"]
                if gd.get("contentType") == "application/pdf":
                    fn = gd.get("filename", "")
                    parent_key = d["key"]
                    return f"/Users/lwj04/Zotero/storage/{parent_key}/{fn}" if fn else None
    return None


# ── Registry helpers ────────────────────────────────────────────────

def load_registry():
    """Load paper registry (DOI/slug → metadata)."""
    path = Path(REGISTRY_PATH)
    if path.exists():
        return json.loads(path.read_text())
    return {}


def build_doi_set(registry):
    """Build set of known DOIs from registry."""
    dois = set()
    for slug, meta in registry.items():
        doi = meta.get("doi", "")
        if doi:
            dois.add(doi.lower().strip())
    return dois


def build_slug_patterns(registry):
    """Build slug patterns for fuzzy matching."""
    patterns = {}
    for slug in registry:
        # Extract year and first author from slug
        m = re.match(r"(\d{4})_(\w+)", slug)
        if m:
            patterns.setdefault(slug, (m.group(1), m.group(2).lower()))
    return patterns


# ── Sync state ──────────────────────────────────────────────────────

def load_sync_state():
    """Load previous sync state."""
    path = Path(SYNC_STATE_PATH)
    if path.exists():
        return json.loads(path.read_text())
    return {"last_sync": None, "processed_keys": [], "sync_log": []}


def save_sync_state(state):
    """Save sync state."""
    path = Path(SYNC_STATE_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2))


# ── Mode: detect ────────────────────────────────────────────────────

def mode_detect(collection="UMo", output_path=None):
    """Detect new items in Zotero that are not in the wiki registry."""
    if output_path is None:
        output_path = "/tmp/zotero_sync_new.json"

    # Determine which collections to scan
    if collection == "all":
        targets = list(COLLECTION_TREE.keys())
    else:
        targets = [collection]

    registry = load_registry()
    known_dois = build_doi_set(registry)
    state = load_sync_state()
    processed_keys = set(state.get("processed_keys", []))

    all_new = []
    stats = {"scanned": 0, "matched_doi": 0, "already_synced": 0, "new": 0, "no_pdf": 0}

    for target in targets:
        tree = COLLECTION_TREE[target]
        keys = [tree["root"]] + tree["subcollections"]
        items = get_collection_items(keys)
        stats["scanned"] += len(items)

        for key, d in items.items():
            # Skip already synced
            if key in processed_keys:
                stats["already_synced"] += 1
                continue

            # Match by DOI
            doi = d.get("DOI", "").lower().strip()
            if doi and doi in known_dois:
                stats["matched_doi"] += 1
                processed_keys.add(key)
                continue

            # Get PDF
            pdf_path = get_pdf_path(key)

            # Extract metadata
            creators = d.get("creators", [])
            first_author = ""
            for c in creators:
                if c.get("lastName"):
                    first_author = c["lastName"]
                    break
                elif c.get("name"):
                    first_author = c["name"].split()[0]
                    break

            year = d.get("date", "")[:4]
            item_type = d.get("itemType", "")

            # Generate slug
            if first_author and year:
                short_title = re.sub(r"[^a-zA-Z0-9]", "", d.get("title", "")[:20])
                slug = f"{year}_{first_author}_{short_title}"
            else:
                slug = f"zotero_{key}"

            entry = {
                "zotero_key": key,
                "collection": target,
                "slug": slug,
                "title": d.get("title", ""),
                "doi": d.get("DOI", ""),
                "first_author": first_author,
                "year": year,
                "item_type": item_type,
                "date_added": d.get("dateAdded", ""),
                "pdf_path": pdf_path,
                "has_pdf": pdf_path is not None,
            }

            if not pdf_path:
                stats["no_pdf"] += 1

            all_new.append(entry)
            stats["new"] += 1

        print(f"  {tree['name']}: {len(items)} items scanned")

    # Sort: with PDF first, then by date
    all_new.sort(key=lambda x: (not x["has_pdf"], x.get("date_added", "")), reverse=True)

    # Save results
    result = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "stats": stats,
        "new_items": all_new,
    }
    with open(output_path, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # Update sync state
    state["processed_keys"] = list(processed_keys)
    state["sync_log"].append({
        "timestamp": result["timestamp"],
        "collection": collection,
        "scanned": stats["scanned"],
        "new": stats["new"],
        "no_pdf": stats["no_pdf"],
    })
    # Keep last 50 sync logs
    state["sync_log"] = state["sync_log"][-50:]
    save_sync_state(state)

    # Print summary
    print(f"\n{'='*50}")
    print(f"Zotero Sync Detection Report")
    print(f"{'='*50}")
    print(f"Collection(s): {', '.join(targets)}")
    print(f"Scanned: {stats['scanned']}")
    print(f"Already synced: {stats['already_synced']}")
    print(f"Matched by DOI (in registry): {stats['matched_doi']}")
    print(f"New items: {stats['new']}")
    print(f"  ├─ With PDF: {stats['new'] - stats['no_pdf']}")
    print(f"  └─ No PDF: {stats['no_pdf']}")
    print(f"\nResults saved to: {output_path}")

    return result


# ── Mode: status ────────────────────────────────────────────────────

def mode_status():
    """Show sync status."""
    state = load_sync_state()
    registry = load_registry()

    print(f"{'='*50}")
    print(f"Zotero Sync Status")
    print(f"{'='*50}")
    print(f"Registry papers: {len(registry)}")
    print(f"Processed Zotero keys: {len(state.get('processed_keys', []))}")
    print(f"Last sync: {state.get('last_sync', 'Never')}")

    if state.get("sync_log"):
        print(f"\nRecent sync history:")
        for log in state["sync_log"][-5:]:
            print(f"  {log['timestamp']}: {log['collection']} "
                  f"scanned={log['scanned']} new={log['new']} no_pdf={log['no_pdf']}")


# ── Mode: convert ───────────────────────────────────────────────────

def mode_convert(input_path="/tmp/zotero_sync_new.json"):
    """Convert detected new items' PDFs to markdown for ingest."""
    with open(input_path) as f:
        result = json.load(f)

    new_items = result.get("new_items", [])
    with_pdf = [i for i in new_items if i["has_pdf"]]

    print(f"Items with PDF to convert: {len(with_pdf)}")
    for item in with_pdf:
        pdf = item["pdf_path"]
        if not os.path.exists(pdf):
            print(f"  ⚠️ PDF not found: {pdf}")
            continue
        size_mb = os.path.getsize(pdf) / (1024 * 1024)
        print(f"  {item['slug'][:40]:40s}  {size_mb:6.1f}MB  {os.path.basename(pdf)[:50]}")

    print(f"\nRun ingest pipeline on these items next.")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zotero → LLM Wiki Sync")
    parser.add_argument("--mode", choices=["detect", "convert", "status"], required=True)
    parser.add_argument("--collection", choices=["UMo", "UZr", "all"], default="UMo")
    parser.add_argument("--output", default="/tmp/zotero_sync_new.json")
    parser.add_argument("--input", default="/tmp/zotero_sync_new.json")
    args = parser.parse_args()

    if args.mode == "detect":
        mode_detect(args.collection, args.output)
    elif args.mode == "convert":
        mode_convert(args.input)
    elif args.mode == "status":
        mode_status()
