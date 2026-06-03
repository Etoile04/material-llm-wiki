"""Tests for scripts/slowlane_backfill.py"""

from __future__ import annotations

from unittest.mock import patch

import pytest

from scripts.slowlane_backfill import (
    BackfillResult,
    BackfillSummary,
    backfill_l1,
    backfill_l2,
    run_slowlane_backfill,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_VALUES = [
    {
        "element_system": "U-10Zr",
        "phase": "BCC",
        "property": "density",
        "value": 15.9,
        "unit": "g/cm³",
        "method": "Experiment",
        "source": "Hofman 1990",
        "confidence": "high",
    },
    {
        "element_system": "U-10Zr",
        "phase": "BCC",
        "property": "melting_point",
        "value": 1400,
        "unit": "K",
        "method": "Experiment",
        "source": "Karahan 2013",
        "confidence": "medium",
    },
]

EXISTING_RECORD = {
    "element_system": "U-10Zr",
    "phase": "BCC",
    "property": "density",
    "method": "Experiment",
    "source": "Hofman 1990",
}

NFMD_FORMAT_VALUES = [
    {
        "material_raw": "U-10Zr",
        "name": "density",
        "symbol": "ρ",
        "value_scalar": 15.9,
        "unit": "g/cm³",
        "temperature_k": 298,
        "method": "Experiment",
        "source_file": "Hofman 1990",
    },
]


# ---------------------------------------------------------------------------
# Tests: backfill_l1
# ---------------------------------------------------------------------------


@patch("scripts.slowlane_backfill.write_ref_value")
def test_backfill_l1_writes_high_confidence(mock_write):
    """confidence='high' 的值被写入 (written_auto)."""
    from scripts.write_ref_value import WriteResult, WriteStatus
    mock_write.return_value = WriteResult(
        status=WriteStatus.WRITTEN_AUTO, reason="high confidence"
    )

    result = backfill_l1(SAMPLE_VALUES[:1])

    assert result.written == 1
    assert result.skipped == 0
    assert result.errors == []


@patch("scripts.slowlane_backfill.write_ref_value")
def test_backfill_l1_skips_duplicates(mock_write):
    """已存在的值被跳过 (duplicate)."""
    from scripts.write_ref_value import WriteStatus, WriteResult

    mock_write.return_value = WriteResult(
        status=WriteStatus.DUPLICATE, reason="duplicate record"
    )

    result = backfill_l1(SAMPLE_VALUES[:1], _existing=[EXISTING_RECORD])

    assert result.written == 0
    assert result.skipped == 1


# ---------------------------------------------------------------------------
# Tests: backfill_l2
# ---------------------------------------------------------------------------


@patch("scripts.slowlane_backfill._supabase_insert")
def test_backfill_l2_adapts_format(mock_insert):
    """NFMD 格式转换并写入 Supabase."""
    mock_insert.return_value = "test-uuid-123"

    result = backfill_l2(SAMPLE_VALUES[:1])

    assert result.written == 1
    assert result.skipped == 0
    assert result.errors == []
    mock_insert.assert_called_once()
    # Verify the row mapping
    call_args = mock_insert.call_args[0][0]
    assert call_args["material"] == "U-10Zr"
    assert call_args["structure"] == "BCC"
    assert call_args["property_name"] == "density"
    assert call_args["value"] == 15.9


@patch("scripts.slowlane_backfill._supabase_insert")
def test_backfill_l2_skips_existing(mock_insert):
    """Supabase INSERT 重复时记为 skipped."""
    mock_insert.side_effect = RuntimeError("Supabase INSERT failed (409): duplicate key")

    result = backfill_l2(SAMPLE_VALUES[:1])

    assert result.written == 0
    assert result.skipped == 1
    assert len(result.errors) == 0


# ---------------------------------------------------------------------------
# Tests: run_slowlane_backfill
# ---------------------------------------------------------------------------


@patch("scripts.slowlane_backfill.backfill_l2")
@patch("scripts.slowlane_backfill.backfill_l1")
def test_run_slowlane_backfill_summary(mock_l1, mock_l2):
    """统一入口返回正确汇总."""
    mock_l1.return_value = BackfillResult(written=2, skipped=1)
    mock_l2.return_value = BackfillResult(written=1, skipped=0)

    summary = run_slowlane_backfill(SAMPLE_VALUES)

    assert summary.total_input == len(SAMPLE_VALUES)
    assert summary.l1.written == 2
    assert summary.l1.skipped == 1
    assert summary.l2.written == 1
    assert summary.l2.skipped == 0


def test_empty_input_returns_empty():
    """空输入返回零结果."""
    summary = run_slowlane_backfill([])

    assert summary.total_input == 0
    assert summary.l1.written == 0
    assert summary.l1.skipped == 0
    assert summary.l2.written == 0
    assert summary.l2.skipped == 0
    assert summary.l1.errors == []
    assert summary.l2.errors == []
