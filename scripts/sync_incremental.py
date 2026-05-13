#!/usr/bin/env python3
"""
Incremental Sync: JSON parameter files → Supabase PostgreSQL.

Reads .last_sync timestamp, scans for changed JSON files, upserts parameters.

Logic:
1. Read .last_sync → epoch seconds (0 if missing)
2. Scan JSON dir for files with mtime > last_sync
3. Parse each file → parameter array
4. UPSERT each parameter via REST API (PATCH + Prefer: resolution=merge-duplicates)
   OR via SQL INSERT ON CONFLICT
5. Update .last_sync to current time
6. Print sync report

JSON field → DB column mapping (handles heterogeneous formats):
  id              → id
  name            → name
  name_en         → name_en  (or name_zh if Chinese detected)
  symbol          → symbol
  category        → category
  subcategory     → subcategory
  value_type      → value_type
  value / scalar  → value_scalar (for scalar type)
  range.min       → value_min (for range type)
  range.max       → value_max (for range type)
  value_expr      → value_expr (for expression type)
  values          → value_list (JSON, for list type)
  value           → value_list (if list type and value is array)
  unit            → unit
  uncertainty     → uncertainty
  material        → material_raw
  temperature     → temperature_str
  temperature_K   → temperature_k
  burnup_range    → burnup_range
  method          → method
  confidence      → confidence
  source_file     → source_file
  equation        → equation
  notes / note / description → notes
  conditions      → notes (appended)
  phase           → notes (appended)
  source_paper    → notes (appended)

Usage:
    python3 scripts/sync_incremental.py [--full]
    python3 scripts/sync_incremental.py --full   # sync all files regardless of mtime
"""

import json
import os
import sys
import time
import glob
import subprocess
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

# ── Config ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LAST_SYNC_FILE = os.path.join(SCRIPT_DIR, ".last_sync")
WORKSPACE = os.path.dirname(SCRIPT_DIR)
JSON_DIRS = [
    os.path.join(WORKSPACE, "data", "fuel_swelling_wiki", "parameters"),
    os.path.join(WORKSPACE, "data", "fuel_swelling_wiki", "parameters_v2_snippets"),
]
REPORTS_DIR = os.path.join(WORKSPACE, "reports")

SUPABASE_URL = "http://localhost:54321/rest/v1"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImV4cCI6MTk4MzgxMjk5Nn0.EGIM96RAZx35lJzdJsyH-qQwv8Hdp7fsn3W0YpN81IU"
PSQL_CMD = ["docker", "exec", "-i", "supabase_db_workspace", "psql", "-U", "postgres", "-d", "postgres"]

CST = timezone(timedelta(hours=8))

# ── Helpers ─────────────────────────────────────────────────────────────────

def log(msg: str):
    ts = datetime.now(CST).strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")


def run_sql(sql: str) -> str:
    """Execute SQL via docker psql."""
    try:
        result = subprocess.run(
            PSQL_CMD,
            input=sql,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        log("⚠ SQL timeout")
        return ""


def rest_request(method: str, path: str, data=None, params=None):
    """Make Supabase REST API request."""
    url = f"{SUPABASE_URL}{path}"
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{query}"

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal",
    }

    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
    except Exception as e:
        return 0, str(e)


# ── JSON → DB mapping ───────────────────────────────────────────────────────

def is_chinese(text: str) -> bool:
    """Check if text contains Chinese characters."""
    if not text:
        return False
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def map_param(raw: dict) -> dict:
    """Map a JSON parameter object to DB column dict."""
    d = {}

    # Direct mappings
    d["id"] = raw.get("id")
    d["name"] = raw.get("name") or raw.get("parameter")
    d["symbol"] = raw.get("symbol")
    d["category"] = raw.get("category")
    d["subcategory"] = raw.get("subcategory")
    d["value_type"] = raw.get("value_type", "scalar")
    d["unit"] = raw.get("unit")
    d["uncertainty"] = raw.get("uncertainty")
    d["material_raw"] = raw.get("material")
    d["burnup_range"] = raw.get("burnup_range")
    d["method"] = raw.get("method")
    d["confidence"] = raw.get("confidence")
    d["source_file"] = raw.get("source_file")
    d["equation"] = raw.get("equation") or raw.get("formula")

    # name_en / name_zh
    name_en = raw.get("name_en")
    if name_en:
        d["name_en"] = name_en
    if d["name"] and is_chinese(d["name"]):
        d["name_zh"] = d["name"]
        if not name_en:
            d["name_en"] = None

    # Temperature
    temp_k = raw.get("temperature_K") or raw.get("temperature_k")
    temp_str = raw.get("temperature")
    if temp_k is not None:
        try:
            d["temperature_k"] = float(temp_k)
        except (ValueError, TypeError):
            d["temperature_str"] = str(temp_str) if temp_str else None
    elif temp_str is not None:
        d["temperature_str"] = str(temp_str)
        # Try to parse as number
        try:
            d["temperature_k"] = float(temp_str)
        except (ValueError, TypeError):
            pass

    # Value mapping based on value_type
    vt = d["value_type"]
    raw_value = raw.get("value")
    raw_scalar = raw.get("scalar")

    if vt == "scalar":
        if raw_scalar is not None:
            try:
                d["value_scalar"] = float(raw_scalar)
            except (ValueError, TypeError):
                d["value_str"] = str(raw_scalar)
        elif raw_value is not None:
            if isinstance(raw_value, (int, float)):
                try:
                    d["value_scalar"] = float(raw_value)
                except (ValueError, TypeError, OverflowError):
                    d["value_str"] = str(raw_value)
            else:
                try:
                    d["value_scalar"] = float(raw_value)
                except (ValueError, TypeError):
                    d["value_str"] = str(raw_value)

    elif vt == "range":
        range_obj = raw.get("range")
        if isinstance(range_obj, dict):
            d["value_min"] = range_obj.get("min")
            d["value_max"] = range_obj.get("max")
        else:
            d["value_min"] = raw.get("value_min")
            d["value_max"] = raw.get("value_max")

    elif vt == "expression":
        expr = raw.get("value_expr")
        if expr:
            d["value_expr"] = expr
        elif raw_value and isinstance(raw_value, str):
            d["value_expr"] = raw_value

    elif vt == "list":
        list_val = raw.get("values") or raw_value
        if isinstance(list_val, list):
            d["value_list"] = json.dumps(list_val)

    elif vt == "text":
        txt = raw.get("value_text") or raw_value
        if txt and isinstance(txt, str):
            d["value_text"] = txt

    # value_str (fallback for display)
    if "value_str" not in d and raw.get("value_str"):
        d["value_str"] = raw.get("value_str")
    elif "value_str" not in d and raw_value is not None and vt == "scalar":
        d["value_str"] = str(raw_value)

    # Notes: combine multiple sources
    notes_parts = []
    for key in ["notes", "note", "description", "context"]:
        val = raw.get(key)
        if val and isinstance(val, str):
            notes_parts.append(val)
    # Append conditions, phase, source_paper if present
    for key in ["conditions", "phase", "source_paper"]:
        val = raw.get(key)
        if val and isinstance(val, str):
            notes_parts.append(f"{key}: {val}")
    if notes_parts:
        d["notes"] = "; ".join(notes_parts)

    # Remove None values (Supabase REST treats null as "set to null")
    # We only want to set fields that have values
    d = {k: v for k, v in d.items() if v is not None}

    return d


# ── Sync logic ──────────────────────────────────────────────────────────────

def read_last_sync() -> float:
    """Read last sync timestamp."""
    try:
        with open(LAST_SYNC_FILE) as f:
            return float(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0.0


def write_last_sync(ts: float):
    """Write last sync timestamp."""
    with open(LAST_SYNC_FILE, "w") as f:
        f.write(str(ts))


def find_json_files() -> list:
    """Find all JSON files in configured directories."""
    files = []
    for d in JSON_DIRS:
        if os.path.isdir(d):
            files.extend(glob.glob(os.path.join(d, "*.json")))
    return files


def upsert_param_sql(params: list) -> tuple:
    """Upsert parameters via SQL INSERT ON CONFLICT. Returns (updated, inserted, errors)."""
    if not params:
        return 0, 0, 0

    # Build multi-row INSERT
    columns = [
        "id", "name", "name_zh", "name_en", "symbol", "category", "subcategory",
        "value_type", "value_scalar", "value_min", "value_max", "value_expr",
        "value_list", "value_text", "value_str", "unit", "uncertainty",
        "material_raw", "temperature_k", "temperature_str", "burnup_range",
        "method", "confidence", "source_file", "equation", "notes"
    ]

    values_rows = []
    for p in params:
        vals = []
        for col in columns:
            v = p.get(col)
            if v is None:
                vals.append("NULL")
            elif isinstance(v, bool):
                vals.append("TRUE" if v else "FALSE")
            elif isinstance(v, (int, float)):
                vals.append(str(v))
            else:
                # Escape single quotes
                escaped = str(v).replace("'", "''")
                vals.append(f"'{escaped}'")
        values_rows.append(f"({', '.join(vals)})")

    # Build UPDATE SET clause (all columns except id)
    update_cols = [c for c in columns if c != "id"]
    update_set = ", ".join(f"{c} = EXCLUDED.{c}" for c in update_cols)

    # Split into batches of 100 to avoid query size issues
    batch_size = 100
    total_updated = 0
    total_inserted = 0
    total_errors = 0

    for i in range(0, len(values_rows), batch_size):
        batch = values_rows[i:i+batch_size]
        values_sql = ",\n  ".join(batch)

        sql = f"""
        INSERT INTO parameters ({', '.join(columns)})
        VALUES
          {values_sql}
        ON CONFLICT (id) DO UPDATE SET {update_set};
        """

        result = run_sql(sql)
        if "ERROR" in result.upper() if result else False:
            log(f"  ⚠ Batch SQL error: {result[:200]}")
            # Try one by one for this batch
            for j in range(len(batch)):
                single_sql = f"""
                INSERT INTO parameters ({', '.join(columns)})
                VALUES
                  {batch[j]}
                ON CONFLICT (id) DO UPDATE SET {update_set};
                """
                r = run_sql(single_sql)
                if "ERROR" in (r.upper() if r else ""):
                    log(f"  ⚠ Error on param {params[i+j].get('id', '?')}: {r[:200]}")
                    total_errors += 1
                else:
                    # Can't distinguish insert vs update in single mode, count as updated
                    total_updated += 1
        else:
            batch_params = params[i:i+batch_size]
            total_updated += len(batch_params)

    return total_updated, total_inserted, total_errors


def upsert_param_rest(param: dict) -> tuple:
    """Upsert a single parameter via REST API. Returns (success, is_insert)."""
    param_id = param.get("id")
    if not param_id:
        return False, False

    # Try PATCH first (update existing)
    status, body = rest_request(
        "PATCH",
        f"/parameters?id=eq.{param_id}",
        data=param,
    )

    if status == 204:
        # Check if row was actually updated
        status2, body2 = rest_request(
            "GET",
            f"/parameters?id=eq.{param_id}&select=id",
        )
        if status2 == 200:
            rows = json.loads(body2)
            if rows:
                return True, False  # Updated existing

    # If no row updated, try INSERT
    status, body = rest_request(
        "POST",
        "/parameters",
        data=param,
    )

    if status in (201, 204):
        return True, True  # Inserted new

    return False, False


def sync_file(filepath: str) -> tuple:
    """Parse a JSON file and return list of mapped params. Returns (params, error)."""
    try:
        with open(filepath) as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        return [], str(e)

    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        # v2 snippets may have metadata + nested structure
        # Check for known v2 patterns
        if "metadata" in data:
            # v2 format - skip, these are structured differently
            return [], "v2 metadata format (skipped)"
        items = [data]
    else:
        return [], f"Unexpected type: {type(data).__name__}"

    params = []
    for item in items:
        if not isinstance(item, dict):
            continue
        if not item.get("id"):
            continue
        mapped = map_param(item)
        if mapped.get("id"):
            params.append(mapped)

    return params, None


def main():
    full_sync = "--full" in sys.argv

    log("=" * 60)
    log("NFMD Incremental Sync")
    log(f"Mode: {'FULL' if full_sync else 'INCREMENTAL'}")
    log("=" * 60)

    # Step 1: Read last sync time
    last_sync = 0.0 if full_sync else read_last_sync()
    last_sync_str = datetime.fromtimestamp(last_sync, tz=CST).strftime("%Y-%m-%d %H:%M:%S") if last_sync else "never"
    log(f"Last sync: {last_sync_str}")

    # Step 2: Find and filter JSON files
    all_files = find_json_files()
    log(f"Total JSON files found: {len(all_files)}")

    if not full_sync and last_sync > 0:
        changed_files = [f for f in all_files if os.path.getmtime(f) > last_sync]
    else:
        changed_files = all_files

    log(f"Changed/new files (mtime > last_sync): {len(changed_files)}")

    if not changed_files:
        log("No changes detected. Nothing to sync.")
        # Still update timestamp
        write_last_sync(time.time())
        return

    # Step 3: Parse all changed files
    all_params = []
    file_errors = []

    for fp in changed_files:
        params, err = sync_file(fp)
        if err:
            file_errors.append((os.path.basename(fp), err))
        if params:
            all_params.extend(params)

    log(f"Parsed parameters from changed files: {len(all_params)}")
    if file_errors:
        log(f"Files with errors: {len(file_errors)}")
        for fname, err in file_errors[:5]:
            log(f"  ⚠ {fname}: {err[:100]}")

    if not all_params:
        log("No valid parameters to sync.")
        write_last_sync(time.time())
        return

    # Step 4: Upsert to database via SQL (faster than REST for bulk)
    log(f"Upserting {len(all_params)} parameters via SQL...")
    updated, inserted, errors = upsert_param_sql(all_params)
    log(f"  Upserted: {updated}, Errors: {errors}")

    # Step 5: Update last_sync timestamp
    now = time.time()
    write_last_sync(now)
    log(f"Updated .last_sync to {datetime.fromtimestamp(now, tz=CST).strftime('%Y-%m-%d %H:%M:%S')}")

    # Step 6: Print report
    log("")
    log("=" * 60)
    log("SYNC REPORT")
    log("=" * 60)
    log(f"  JSON files scanned:    {len(all_files)}")
    log(f"  Changed files:         {len(changed_files)}")
    log(f"  Parameters upserted:   {updated}")
    log(f"  Parameters inserted:   {inserted}")
    log(f"  Errors:                {errors}")
    log(f"  Files skipped:         {len(file_errors)}")
    if file_errors:
        for fname, err in file_errors:
            log(f"    - {fname}: {err[:80]}")
    log("=" * 60)

    # Verify total
    total_sql = "SELECT count(*) FROM parameters;"
    total = run_sql(total_sql)
    log(f"Database total parameters: {total.strip()}")
    log("✅ Sync complete.")


def detect_new_params(json_dir, last_sync_ts=0):
    """Detect new/changed parameter files since last sync."""
    files = []
    if os.path.isdir(json_dir):
        files = glob.glob(os.path.join(json_dir, "*.json"))
    if last_sync_ts > 0:
        files = [f for f in files if os.path.getmtime(f) > last_sync_ts]
    return files


def build_upsert_batch(params, batch_size=100):
    """Split params into batches for SQL upsert."""
    batches = []
    for i in range(0, len(params), batch_size):
        batches.append(params[i:i+batch_size])
    return batches


def sync_after_ingest(wiki_root=None):
    """Auto-trigger sync after ingest completes."""
    wiki_root = wiki_root or os.environ.get('WIKI_ROOT',
        os.path.join(WORKSPACE, 'data', 'fuel_swelling_wiki'))
    params_dir = os.path.join(wiki_root, 'parameters')

    last_sync = read_last_sync()
    new_files = detect_new_params(params_dir, last_sync)

    if not new_files:
        log("No new parameters to sync after ingest")
        return {"synced": 0, "skipped": True}

    all_params = []
    for fp in new_files:
        params, err = sync_file(fp)
        if err:
            log(f"\u26a0 {os.path.basename(fp)}: {err[:80]}")
        else:
            all_params.extend(params)

    if not all_params:
        log("No valid parameters found")
        return {"synced": 0, "empty": True}

    updated, inserted, errors = upsert_param_sql(all_params)
    write_last_sync(time.time())

    result = {
        "synced": updated,
        "inserted": inserted,
        "errors": errors,
        "files": len(new_files),
    }
    log(f"Post-ingest sync: {updated} upserted, {errors} errors")
    return result


if __name__ == "__main__":
    if "--post-ingest" in sys.argv:
        result = sync_after_ingest()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        main()
