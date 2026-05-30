"""slowlane_backfill: write extracted values into L1 (local PG) and L2 (NFMD Supabase).

L1 write: delegates to write_ref_value.py for quality gate + dedup + confidence write.
L2 write: delegates to adapter_nfmd.py for format conversion (actual Supabase write = TODO).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from scripts.adapter_nfmd import NfmdAdapterError, adapt_nfmd_param
from scripts.write_ref_value import WriteStatus, write_ref_value


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
# L2: NFMD format adaptation
# ---------------------------------------------------------------------------

_DEFAULT_PHASE = "BCC"


def backfill_l2(extracted_values: list[dict[str, Any]]) -> BackfillResult:
    """Adapt extracted values into NFMD format.

    Note: actual Supabase write is a TODO — currently only format conversion.
    """
    result = BackfillResult()

    for val in extracted_values:
        try:
            adapted = adapt_nfmd_param(val, phase=_DEFAULT_PHASE)
            # TODO: actual Supabase INSERT goes here
            result.written += 1
        except NfmdAdapterError as exc:
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
) -> BackfillSummary:
    """Unified backfill entry: L1 + L2."""
    l1 = backfill_l1(extracted_values, _existing=_existing)
    l2 = backfill_l2(extracted_values)

    return BackfillSummary(
        l1=l1,
        l2=l2,
        total_input=len(extracted_values),
    )
