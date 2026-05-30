"""End-to-end tests for the slowline pipeline:
extract → backfill L1+L2 → log → message schema integration.

These tests simulate the full slowline flow using real module logic,
mocking only external I/O (DB, file system outside tmp_path).
"""

from __future__ import annotations

import json
import uuid

import pytest

from scripts.slowlane_backfill import (
    BackfillResult,
    BackfillSummary,
    backfill_l1,
    backfill_l2,
    run_slowlane_backfill,
)
from scripts.write_ref_value import WriteStatus
from scripts.ref_logger import RefLogger
from scripts.message_schemas import (
    GapRequest,
    GapRequestItem,
    DataSet,
    DataSetStats,
    gap_request_to_json,
    gap_request_from_json,
    data_set_to_json,
    data_set_from_json,
    validate_gap_request,
    validate_data_set,
)


# ---------------------------------------------------------------------------
# Shared fixtures / helpers
# ---------------------------------------------------------------------------

def _make_ref(
    element_system: str,
    phase: str,
    property: str,
    value: float,
    unit: str,
    method: str,
    source: str,
    confidence: str,
) -> dict:
    """Build a reference-value dict that passes the quality gate."""
    return dict(
        element_system=element_system,
        phase=phase,
        property=property,
        value=value,
        unit=unit,
        method=method,
        source=source,
        confidence=confidence,
    )


# ═══════════════════════════════════════════════════════════════════════════
# 1. test_slowlane_extracts_and_backfills_l1
# ═══════════════════════════════════════════════════════════════════════════

class TestSlowlaneExtractsAndBackfillsL1:
    """Simulate 3 extracted values (different confidence), call backfill_l1,
    verify high-confidence written, medium written (needs_review), skip duplicates."""

    def test_high_confidence_auto_written(self):
        """High confidence → WRITTEN_AUTO."""
        ref = _make_ref("U-10Zr", "BCC", "C11", 150.0, "GPa", "DFT", "DFT-paper-2024", "high")
        result = backfill_l1([ref])
        assert result.written == 1
        assert result.skipped == 0
        assert len(result.errors) == 0

    def test_medium_confidence_pending_review(self):
        """Medium confidence → WRITTEN_PENDING_REVIEW."""
        ref = _make_ref("U-10Zr", "BCC", "C12", 80.0, "GPa", "DFT", "DFT-paper-2024", "medium")
        result = backfill_l1([ref])
        assert result.written == 1  # still counted as written (pending review)

    def test_duplicate_skipped(self):
        """Second identical value → DUPLICATE (skipped)."""
        ref = _make_ref("U-10Zr", "BCC", "C11", 150.0, "GPa", "DFT", "DFT-paper-2024", "high")
        existing = [ref]
        result = backfill_l1([ref], _existing=existing)
        assert result.skipped == 1
        assert result.written == 0

    def test_mixed_three_values(self):
        """3 values: high (new), medium (new), high (dup) → written=2, skipped=1."""
        ref_high = _make_ref("U-10Zr", "BCC", "C11", 150.0, "GPa", "DFT", "paper-A", "high")
        ref_medium = _make_ref("U-10Zr", "BCC", "C12", 80.0, "GPa", "DFT", "paper-B", "medium")
        ref_dup = _make_ref("U-10Zr", "BCC", "C11", 150.0, "GPa", "DFT", "paper-A", "high")

        result = backfill_l1([ref_high, ref_medium, ref_dup])
        assert result.written == 2
        assert result.skipped == 1


# ═══════════════════════════════════════════════════════════════════════════
# 2. test_slowlane_extracts_and_backfills_l2
# ═══════════════════════════════════════════════════════════════════════════

class TestSlowlaneExtractsAndBackfillsL2:
    """Simulate 2 extracted NFMD values, call backfill_l2, verify NFMD format
    conversion produces correct reference_value fields."""

    def test_l2_adaptation_produces_correct_format(self):
        """NFMD param → reference_value via adapt_nfmd_param inside backfill_l2."""
        nfmd_params = [
            {
                "material_raw": "U-Mo",
                "name": "C11",
                "symbol": "C11",
                "value_scalar": 120.0,
                "unit": "GPa",
                "temperature_k": 300,
                "method": "DFT",
                "source_file": "some-dft-paper.pdf",
            },
            {
                "material_raw": "U-Mo",
                "name": "C12",
                "symbol": "C12",
                "value_scalar": 60.0,
                "unit": "GPa",
                "temperature_k": 300,
                "method": "DFT",
                "source_file": "some-dft-paper.pdf",
            },
        ]

        result = backfill_l2(nfmd_params)
        assert result.written == 2
        assert result.skipped == 0
        assert len(result.errors) == 0


# ═══════════════════════════════════════════════════════════════════════════
# 3. test_slowlane_logs_request
# ═══════════════════════════════════════════════════════════════════════════

class TestSlowlaneLogsRequest:
    """Create RefLogger, start_request → record_cache_hit × 2 → finish_request,
    verify JSON log written correctly."""

    def test_full_request_log_written(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        rid = logger.start_request(items_count=2)
        logger.record_cache_hit("L1")
        logger.record_cache_hit("L2")
        entry = logger.finish_request(duration_seconds=3.5, gaps_remaining=0)

        # Verify returned entry structure
        assert entry["request_id"] == rid
        assert entry["cache_hits"]["L1"] == 1
        assert entry["cache_hits"]["L2"] == 1
        assert entry["cache_hits"]["L3"] == 0
        assert entry["duration_seconds"] == 3.5
        assert entry["items_requested"] == 2
        assert entry["gaps_remaining"] == 0

        # Verify JSON file was written
        today_files = list(tmp_path.glob("*.json"))
        assert len(today_files) == 1

        with open(today_files[0]) as f:
            entries = json.load(f)
        assert len(entries) == 1
        assert entries[0]["request_id"] == rid
        assert entries[0]["cache_hits"]["L1"] == 1

    def test_multiple_requests_append(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        rid1 = logger.start_request(items_count=1)
        logger.finish_request(duration_seconds=1.0, gaps_remaining=1)

        rid2 = logger.start_request(items_count=2)
        logger.record_cache_hit("L1")
        logger.finish_request(duration_seconds=2.0, gaps_remaining=0)

        log_files = list(tmp_path.glob("*.json"))
        assert len(log_files) == 1

        with open(log_files[0]) as f:
            entries = json.load(f)
        assert len(entries) == 2
        assert entries[0]["request_id"] == rid1
        assert entries[1]["request_id"] == rid2


# ═══════════════════════════════════════════════════════════════════════════
# 4. test_slowlane_handles_empty_input
# ═══════════════════════════════════════════════════════════════════════════

class TestSlowlaneHandlesEmptyInput:
    """Empty list to run_slowlane_backfill → zero results."""

    def test_empty_input_returns_zero(self):
        summary = run_slowlane_backfill([])
        assert isinstance(summary, BackfillSummary)
        assert summary.total_input == 0
        assert summary.l1.written == 0
        assert summary.l1.skipped == 0
        assert summary.l2.written == 0
        assert summary.l2.skipped == 0
        assert summary.l1.errors == []
        assert summary.l2.errors == []

    def test_empty_l1_backfill(self):
        result = backfill_l1([])
        assert result.written == 0
        assert result.skipped == 0

    def test_empty_l2_backfill(self):
        result = backfill_l2([])
        assert result.written == 0
        assert result.skipped == 0


# ═══════════════════════════════════════════════════════════════════════════
# 5. test_slowlane_skips_duplicates
# ═══════════════════════════════════════════════════════════════════════════

class TestSlowlaneSkipsDuplicates:
    """Same value backfill_l1 twice → second call skipped == 1."""

    def test_second_call_skips_duplicate(self):
        ref = _make_ref("U-10Zr", "BCC", "C44", 40.0, "GPa", "DFT", "paper-X", "high")

        # First call: written
        result1 = backfill_l1([ref])
        assert result1.written == 1
        assert result1.skipped == 0

        # Second call with same existing: skipped
        # (We need to pass the ref as existing to simulate the dedup)
        result2 = backfill_l1([ref], _existing=[ref])
        assert result2.skipped == 1
        assert result2.written == 0

    def test_similar_but_different_source_not_dup(self):
        """Same everything except source → not a duplicate."""
        ref_a = _make_ref("U-10Zr", "BCC", "C44", 40.0, "GPa", "DFT", "paper-A", "high")
        ref_b = _make_ref("U-10Zr", "BCC", "C44", 40.0, "GPa", "DFT", "paper-B", "high")

        result = backfill_l1([ref_b], _existing=[ref_a])
        assert result.written == 1
        assert result.skipped == 0


# ═══════════════════════════════════════════════════════════════════════════
# 6. test_message_schemas_in_slowlane_context
# ═══════════════════════════════════════════════════════════════════════════

class TestMessageSchemasInSlowlaneContext:
    """Create GapRequest with 2 GapRequestItems (U-Mo BCC C11 + C12),
    verify serialization/deserialization, create DataSet with backfill results,
    verify status and stats."""

    @pytest.fixture()
    def gap_request(self) -> GapRequest:
        return GapRequest(items=[
            GapRequestItem(
                element_system="U-Mo",
                phase="BCC",
                properties=["C11", "C12"],
                preferred_method="DFT",
            ),
            GapRequestItem(
                element_system="U-Mo",
                phase="BCC",
                properties=["bulk_modulus"],
                preferred_method="any",
            ),
        ])

    def test_gap_request_valid(self, gap_request):
        errors = validate_gap_request(gap_request)
        assert errors == []

    def test_gap_request_serialization_roundtrip(self, gap_request):
        json_str = gap_request_to_json(gap_request)
        parsed = gap_request_from_json(json_str)
        assert parsed.request_id == gap_request.request_id
        assert parsed.schema_version == gap_request.schema_version
        assert len(parsed.items) == 2
        assert parsed.items[0].element_system == "U-Mo"
        assert parsed.items[0].properties == ["C11", "C12"]
        assert parsed.items[0].phase == "BCC"
        assert parsed.items[1].properties == ["bulk_modulus"]

    def test_data_set_with_backfill_results(self, gap_request):
        """Create DataSet representing partial backfill results."""
        ds = DataSet(
            request_id=gap_request.request_id,
            status="partial",
            stats=DataSetStats(
                total_requested=3,   # C11 + C12 + bulk_modulus
                from_cache=1,        # one from cache
                from_express=1,      # one from express
                gaps_remaining=1,     # bulk_modulus still missing
            ),
            data=[
                _make_ref("U-Mo", "BCC", "C11", 120.0, "GPa", "DFT", "paper-Y", "high"),
            ],
            gaps=[
                {
                    "element_system": "U-Mo",
                    "phase": "BCC",
                    "property": "bulk_modulus",
                    "reason": "not found in L1/L2/L3",
                },
            ],
        )

        # Validate DataSet
        errors = validate_data_set(ds)
        assert errors == []

        # Verify stats
        assert ds.stats.total_requested == 3
        assert ds.stats.from_cache == 1
        assert ds.stats.from_express == 1
        assert ds.stats.gaps_remaining == 1

        # Verify status
        assert ds.status == "partial"

    def test_data_set_serialization_roundtrip(self, gap_request):
        ds = DataSet(
            request_id=gap_request.request_id,
            status="complete",
            stats=DataSetStats(total_requested=3, from_cache=3, from_express=0, gaps_remaining=0),
            data=[
                _make_ref("U-Mo", "BCC", "C11", 120.0, "GPa", "DFT", "paper-Y", "high"),
                _make_ref("U-Mo", "BCC", "C12", 60.0, "GPa", "DFT", "paper-Y", "high"),
                _make_ref("U-Mo", "BCC", "bulk_modulus", 80.0, "GPa", "DFT", "paper-Y", "high"),
            ],
            gaps=[],
        )

        json_str = data_set_to_json(ds)
        parsed = data_set_from_json(json_str)

        assert parsed.request_id == ds.request_id
        assert parsed.status == "complete"
        assert parsed.stats.total_requested == 3
        assert parsed.stats.from_cache == 3
        assert parsed.stats.gaps_remaining == 0
        assert len(parsed.data) == 3
