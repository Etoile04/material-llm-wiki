"""slowlane_backfill: write extracted values into L1 (local PG) and L2 (NFMD Supabase).

L1 write: delegates to write_ref_value.py for quality gate + dedup + confidence write.
L2 write: delegates to adapter_nfmd.py for format conversion, then POSTs to Supabase.
"""

from __future__ import annotations

import json
import os
import urllib.request
import urllib.error
from dataclasses import dataclass, field
from typing import Any, Optional

from scripts.adapter_nfmd import NfmdAdapterError, adapt_nfmd_param
from scripts.write_ref_value import WriteStatus, write_ref_value


# ---------------------------------------------------------------------------
# Supabase config
# ---------------------------------------------------------------------------

_SUPABASE_URL = os.getenv("SUPABASE_URL", "http://127.0.0.1:54421")
_SUPABASE_ANON_KEY = os.getenv(
    "SUPABASE_ANON_KEY",
    "sb_publishable_ACJWlzQHlZjBrEguHvfOxg_3BJgxAaH",
)
_SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class BackfillResult:
    written: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)


@dataclass
class BackfillSummary:
    l1: BackfillResult
    l2: BackfillResult
    total_input: int = 0


# ---------------------------------------------------------------------------
# L1: local PG write
# ---------------------------------------------------------------------------


def backfill_l1(
    extracted_values: list[dict[str, Any]],
    _existing: list[dict[str, Any]] | None = None,
) -> BackfillResult:
    """Write extracted values into L1 (reference_values).

    Delegates to write_ref_value() for quality gate, dedup, and
    confidence-based write decision.
    """
    result = BackfillResult()
    existing = _existing if _existing is not None else []

    for ref in extracted_values:
        try:
            wr = write_ref_value(ref, _existing=existing)
            if wr.status in (WriteStatus.WRITTEN_AUTO, WriteStatus.WRITTEN_PENDING_REVIEW):
                result.written += 1
                # Append to existing so subsequent values can dedup against it
                existing.append(ref)
            elif wr.status == WriteStatus.DUPLICATE:
                result.skipped += 1
            else:
                # REJECTED — count as error
                result.errors.append(wr.reason)
        except Exception as exc:
            result.errors.append(str(exc))

    return result


# ---------------------------------------------------------------------------
# L2: NFMD format adaptation + Supabase INSERT
# ---------------------------------------------------------------------------

_DEFAULT_PHASE = "BCC"


def _supabase_insert(row: dict, *, table: str = "reference_values") -> Optional[str]:
    """INSERT a single row into Supabase. Returns the row id or None on failure."""
    key = _SUPABASE_SERVICE_KEY or _SUPABASE_ANON_KEY
    payload = json.dumps(row).encode("utf-8")
    req = urllib.request.Request(
        f"{_SUPABASE_URL}/rest/v1/{table}",
        data=payload,
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read())
            return body[0]["id"] if body else None
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Supabase INSERT failed ({e.code}): {detail}") from e


def _ref_to_nucpot_row(ref: dict) -> dict:
    """Map ref-gap-fill format → nucpot reference_values schema.

    ref-gap-fill: element_system, phase, property, value, unit, method, source, confidence, temperature
    nucpot:       material,     structure, property_name, value, unit, source, temperature, notes
    """
    return {
        "material": ref["element_system"],
        "structure": ref.get("phase", "BCC"),
        "property_name": ref["property"],
        "value": ref["value"],
        "unit": ref["unit"],
        "source": ref.get("source", ""),
        "temperature": ref.get("temperature", 0),
        "notes": json.dumps({
            "method": ref.get("method", ""),
            "confidence": ref.get("confidence", ""),
            "cache_level": ref.get("cache_level", "L1"),
        }) if ref.get("method") or ref.get("confidence") else None,
    }


def backfill_l2(
    extracted_values: list[dict[str, Any]],
    *,
    dry_run: bool = False,
) -> BackfillResult:
    """Adapt extracted values into nucpot reference_values schema and write to Supabase.

    Accepts two formats:
      - ref-gap-fill format: element_system, phase, property, value, unit, ...
      - NFMD raw format: material_raw, name, symbol, value_scalar, unit, ...

    For NFMD raw format, adapt_nfmd_param() is called first to convert to
    ref-gap-fill format before mapping to nucpot schema.
    """
    result = BackfillResult()

    for val in extracted_values:
        try:
            # Auto-detect format: NFMD raw has 'material_raw', ref-gap-fill has 'element_system'
            if "material_raw" in val and "element_system" not in val:
                adapted = adapt_nfmd_param(val, phase=_DEFAULT_PHASE)
                row = _ref_to_nucpot_row(adapted)
            elif "element_system" in val:
                row = _ref_to_nucpot_row(val)
            else:
                raise ValueError(f"Unrecognized format: keys={list(val.keys())}")

            if dry_run:
                result.written += 1
                continue
            _supabase_insert(row)
            result.written += 1
        except RuntimeError as exc:
            err_msg = str(exc)
            if "409" in err_msg or "duplicate" in err_msg.lower():
                result.skipped += 1
            else:
                result.errors.append(err_msg)
        except (NfmdAdapterError, ValueError) as exc:
            result.errors.append(str(exc))
        except Exception as exc:
            result.errors.append(str(exc))

    return result


# ---------------------------------------------------------------------------
# Unified entry point
# ---------------------------------------------------------------------------


def run_slowlane_backfill(
    extracted_values: list[dict[str, Any]],
    _existing: list[dict[str, Any]] | None = None,
    *,
    dry_run: bool = False,
) -> BackfillSummary:
    """Unified backfill entry: L1 + L2."""
    l1 = backfill_l1(extracted_values, _existing=_existing)
    l2 = backfill_l2(extracted_values, dry_run=dry_run)

    return BackfillSummary(
        l1=l1,
        l2=l2,
        total_input=len(extracted_values),
    )
