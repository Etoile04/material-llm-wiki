#!/usr/bin/env python3
"""
Zotero → LLM Wiki Auto-Sync
Detects new/updated items in Zotero collections and prepares them for ingest.

Usage:
  python3 zotero_sync.py --mode detect [--collection UMo|UZr|all] [--output /tmp/sync_result.json]
  python3 zotero_sync.py --mode enrich-pdf --input /tmp/sync_result.json   # add PDF paths to detected items
  python3 zotero_sync.py --mode preview --input /tmp/sync_result.json      # preview items with PDFs
  python3 zotero_sync.py --mode status

Changelog:
  v2 (2026-05-01): Code review fixes — C1 (PDF scan separated), C2 (health check),
    C3 (processed_keys cap), I3 (slug fuzzy match), I4 (last_sync), I5 (atomic write),
    I6 (convert→preview), I2 (env var path).
"""

import argparse
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────
ZOTERO_API = os.environ.get("ZOTERO_API", "http://localhost:23119/api/users/0")
ZOTERO_STORAGE = os.environ.get("ZOTERO_STORAGE", "/Users/lwj04/Zotero/storage")
WIKI_ROOT = os.environ.get("WIKI_ROOT", "data/fuel_swelling_wiki")
REGISTRY_PATH = os.path.join(WIKI_ROOT, "paper_registry.json")
SYNC_STATE_PATH = os.path.join(WIKI_ROOT, "zotero_sync_state.json")
API_DELAY = float(os.environ.get("ZOTERO_API_DELAY", "0.05"))  # seconds between API calls
MAX_PROCESSED_KEYS = 2000  # cap for processed_keys set

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

def check_zotero_alive():
    """Verify Zotero local API is reachable. Exit with error if not."""
    try:
        resp = urllib.request.urlopen(f"{ZOTERO_API}/items?limit=1", timeout=5)
        return resp.status == 200
    except Exception as e:
        print(f"ERROR: Zotero local API unreachable at {ZOTERO_API}", file=sys.stderr)
        print(f"  {e}", file=sys.stderr)
        print(f"  Make sure Zotero is running.", file=sys.stderr)
        return False


def api_get(path, **params):
    """GET from Zotero local API with retry."""
    qs = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{ZOTERO_API}{path}?{qs}" if qs else f"{ZOTERO_API}{path}"

    for attempt in range(3):
        try:
            resp = urllib.request.urlopen(url, timeout=30)
            return json.loads(resp.read())
        except urllib.error.URLError as e:
            if attempt < 2:
                time.sleep(0.5 * (attempt + 1))
                continue
            print(f"API error (URLError, {attempt+1} retries): {url} → {e}", file=sys.stderr)
            return []
        except json.JSONDecodeError as e:
            print(f"API error (bad JSON): {url} → {e}", file=sys.stderr)
            return []
        except Exception as e:
            print(f"API error: {url} → {e}", file=sys.stderr)
            return []
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
            time.sleep(API_DELAY)
    return all_items


def get_pdf_path(item_key):
    """Find PDF attachment path for an item. Returns (path, size_bytes) or (None, 0).

    Zotero stores PDFs at /storage/{ATTACHMENT_KEY}/{filename}, not the parent item key.
    """
    children = api_get(f"/items/{item_key}/children", format="json")
    for child in children:
        d = child["data"]
        if d.get("contentType") == "application/pdf" and d.get("linkMode", "").startswith("imported"):
            filename = d.get("filename", "")
            att_key = d["key"]  # attachment key, not parent item key
            if filename:
                path = f"{ZOTERO_STORAGE}/{att_key}/{filename}"
                size = os.path.getsize(path) if os.path.exists(path) else 0
                return path, size
            return None, 0
    return None, 0


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


def build_slug_index(registry):
    """Build index: (year, first_author_lower) → set of slugs for fuzzy matching."""
    index = {}
    for slug in registry:
        m = re.match(r"(\d{4})_(\w+)", slug)
        if m:
            key = (m.group(1), m.group(2).lower())
            index.setdefault(key, set()).add(slug)
    return index


def match_by_slug(item, slug_index):
    """Try to match an item against existing registry slugs by year+author."""
    creators = item.get("creators", [])
    first_author = ""
    for c in creators:
        if c.get("lastName"):
            first_author = c["lastName"].lower()
            break
        elif c.get("name"):
            first_author = c["name"].split()[0].lower()
            break

    year = item.get("date", "")[:4]
    if first_author and year:
        key = (year, first_author)
        if key in slug_index:
            return True
    return False


# ── Sync state ──────────────────────────────────────────────────────

def load_sync_state():
    """Load previous sync state."""
    path = Path(SYNC_STATE_PATH)
    if path.exists():
        return json.loads(path.read_text())
    return {"last_sync": None, "processed_keys": [], "sync_log": []}


def save_sync_state(state):
    """Save sync state atomically."""
    path = Path(SYNC_STATE_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Cap processed_keys to prevent unbounded growth [C3]
    if len(state["processed_keys"]) > MAX_PROCESSED_KEYS:
        state["processed_keys"] = state["processed_keys"][-MAX_PROCESSED_KEYS:]
    # Atomic write [I5]
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".json")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
    except Exception:
        os.unlink(tmp)
        raise


# ── Metadata extraction ────────────────────────────────────────────

def extract_author_year(item_data):
    """Extract first author and year from Zotero item data."""
    creators = item_data.get("creators", [])
    first_author = ""
    for c in creators:
        if c.get("lastName"):
            first_author = c["lastName"]
            break
        elif c.get("name"):
            first_author = c["name"].split()[0]
            break
    year = item_data.get("date", "")[:4]
    return first_author, year


def generate_slug(first_author, year, title, zotero_key):
    """Generate a wiki-compatible slug. Falls back to zotero_key for non-ASCII titles."""
    if first_author and year:
        short_title = re.sub(r"[^a-zA-Z0-9]", "", title[:20])
        if short_title:  # non-empty after stripping (ASCII content)
            return f"{year}_{first_author}_{short_title}"
    return f"zotero_{zotero_key}"


# ── Mode: detect ────────────────────────────────────────────────────

def mode_detect(collection="UMo", output_path=None):
    """Detect new items in Zotero that are not in the wiki registry.

    This mode does NOT query PDF paths (performance optimization [C1]).
    Use --mode enrich-pdf separately to add PDF info.
    """
    # Health check [C2]
    if not check_zotero_alive():
        sys.exit(1)

    if output_path is None:
        output_path = "/tmp/zotero_sync_new.json"

    # Determine which collections to scan
    if collection == "all":
        targets = list(COLLECTION_TREE.keys())
    else:
        targets = [collection]

    registry = load_registry()
    known_dois = build_doi_set(registry)
    slug_index = build_slug_index(registry)  # [I3]
    state = load_sync_state()
    processed_keys = set(state.get("processed_keys", []))

    all_new = []
    stats = {
        "scanned": 0, "matched_doi": 0, "matched_slug": 0,
        "already_synced": 0, "new": 0,
    }

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

            # Match by slug (year+author) [I3]
            if match_by_slug(d, slug_index):
                stats["matched_slug"] += 1
                processed_keys.add(key)
                continue

            # Extract metadata
            first_author, year = extract_author_year(d)
            slug = generate_slug(first_author, year, d.get("title", ""), key)

            entry = {
                "zotero_key": key,
                "collection": target,
                "slug": slug,
                "title": d.get("title", ""),
                "doi": d.get("DOI", ""),
                "first_author": first_author,
                "year": year,
                "item_type": d.get("itemType", ""),
                "date_added": d.get("dateAdded", ""),
            }

            all_new.append(entry)
            stats["new"] += 1

        print(f"  {tree['name']}: {len(items)} items scanned")

    # Sort by date
    all_new.sort(key=lambda x: x.get("date_added", ""), reverse=True)

    # Save results
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S")
    result = {
        "timestamp": timestamp,
        "collection": collection,
        "stats": stats,
        "new_items": all_new,
    }

    # Write sync state BEFORE output file [I5]
    state["last_sync"] = timestamp  # [I4]
    state["processed_keys"] = list(processed_keys)
    state["sync_log"].append({
        "timestamp": timestamp,
        "collection": collection,
        "scanned": stats["scanned"],
        "new": stats["new"],
        "matched_doi": stats["matched_doi"],
        "matched_slug": stats["matched_slug"],
    })
    state["sync_log"] = state["sync_log"][-50:]
    save_sync_state(state)

    # Write output file
    with open(output_path, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # Print summary
    print(f"\n{'='*50}")
    print(f"Zotero Sync Detection Report")
    print(f"{'='*50}")
    print(f"Collection(s): {', '.join(targets)}")
    print(f"Scanned: {stats['scanned']}")
    print(f"Already synced: {stats['already_synced']}")
    print(f"Matched by DOI: {stats['matched_doi']}")
    print(f"Matched by slug: {stats['matched_slug']}")
    print(f"New items: {stats['new']}")
    print(f"\nResults saved to: {output_path}")
    print(f"Next: python3 zotero_sync.py --mode enrich-pdf --input {output_path}")

    return result


# ── Mode: enrich-pdf ────────────────────────────────────────────────

def mode_enrich_pdf(input_path="/tmp/zotero_sync_new.json", output_path=None):
    """Add PDF paths to detected items. Separate step for performance [C1]."""
    if not check_zotero_alive():
        sys.exit(1)

    if output_path is None:
        output_path = input_path

    with open(input_path) as f:
        result = json.load(f)

    new_items = result.get("new_items", [])
    total = len(new_items)
    with_pdf = 0
    no_pdf = 0

    for i, item in enumerate(new_items):
        if (i + 1) % 20 == 0:
            print(f"  Progress: {i+1}/{total}...")
        pdf_path, pdf_size = get_pdf_path(item["zotero_key"])
        item["pdf_path"] = pdf_path
        item["has_pdf"] = pdf_path is not None
        item["pdf_size_mb"] = round(pdf_size / (1024 * 1024), 1) if pdf_size else 0
        if pdf_path:
            with_pdf += 1
        else:
            no_pdf += 1
        time.sleep(API_DELAY)

    # Sort: with PDF first
    new_items.sort(key=lambda x: (not x["has_pdf"], x.get("date_added", "")), reverse=True)
    result["stats"]["with_pdf"] = with_pdf
    result["stats"]["no_pdf"] = no_pdf

    with open(output_path, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*50}")
    print(f"PDF Enrichment Complete")
    print(f"{'='*50}")
    print(f"Total items: {total}")
    print(f"With PDF: {with_pdf}")
    print(f"No PDF: {no_pdf}")
    print(f"Results saved to: {output_path}")


# ── Mode: preview ───────────────────────────────────────────────────

def mode_preview(input_path="/tmp/zotero_sync_new.json"):
    """Preview detected items with PDF info [I6: renamed from convert]."""
    with open(input_path) as f:
        result = json.load(f)

    new_items = result.get("new_items", [])
    with_pdf = [i for i in new_items if i.get("has_pdf")]
    no_pdf = [i for i in new_items if not i.get("has_pdf")]

    print(f"{'='*50}")
    print(f"Sync Preview: {result.get('timestamp', '?')}")
    print(f"{'='*50}")
    print(f"Total new items: {len(new_items)}")
    print(f"With PDF: {len(with_pdf)}")
    print(f"No PDF: {len(no_pdf)}")

    if no_pdf:
        print(f"\n--- Items without PDF ({len(no_pdf)}) ---")
        for item in no_pdf[:10]:
            print(f"  {item.get('first_author','?')} {item.get('year','?')}  {item['title'][:60]}")
        if len(no_pdf) > 10:
            print(f"  ... and {len(no_pdf) - 10} more")

    if with_pdf:
        total_size = sum(i.get("pdf_size_mb", 0) for i in with_pdf)
        print(f"\n--- Items with PDF ({len(with_pdf)}, {total_size:.0f}MB total) ---")
        for item in with_pdf[:20]:
            print(f"  {item['slug'][:40]:40s}  {item.get('pdf_size_mb',0):6.1f}MB  {os.path.basename(item.get('pdf_path',''))[:50]}")
        if len(with_pdf) > 20:
            print(f"  ... and {len(with_pdf) - 20} more")

    print(f"\nNext: Run ingest pipeline on these items.")


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
                  f"scanned={log['scanned']} new={log['new']} "
                  f"doi={log.get('matched_doi', 0)} slug={log.get('matched_slug', 0)}")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zotero → LLM Wiki Sync")
    parser.add_argument("--mode", choices=["detect", "enrich-pdf", "preview", "status"], required=True)
    parser.add_argument("--collection", choices=["UMo", "UZr", "all"], default="UMo")
    parser.add_argument("--output", default="/tmp/zotero_sync_new.json")
    parser.add_argument("--input", default="/tmp/zotero_sync_new.json")
    args = parser.parse_args()

    if args.mode == "detect":
        mode_detect(args.collection, args.output)
    elif args.mode == "enrich-pdf":
        mode_enrich_pdf(args.input, args.output)
    elif args.mode == "preview":
        mode_preview(args.input)
    elif args.mode == "status":
        mode_status()
