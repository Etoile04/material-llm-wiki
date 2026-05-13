#!/bin/bash
# Post-ingest hook: automatically sync new parameters to Supabase
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WIKI_ROOT="${WIKI_ROOT:-/Users/lwj04/.openclaw/workspace/data/fuel_swelling_wiki}"
echo "[post-ingest] Auto-triggering Supabase sync..."
python3 "${SCRIPT_DIR}/sync_incremental.py" --post-ingest 2>&1 | tee "${SCRIPT_DIR}/.last_sync_report.json"
echo "[post-ingest] Done."
