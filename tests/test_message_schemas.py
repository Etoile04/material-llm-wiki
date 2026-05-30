import json
import uuid
import pytest
from scripts.message_schemas import (
    GapRequest, GapRequestItem, DataSet, DataSetStats,
    gap_request_to_json, gap_request_from_json,
    data_set_to_json, data_set_from_json,
    validate_gap_request, validate_data_set,
)


class TestGapRequestItem:
    def test_gap_request_item_requires_element_system(self):
        item = GapRequestItem(element_system="", properties=["C11"])
        req = GapRequest(items=[item])
        errors = validate_gap_request(req)
        assert any("element_system" in e for e in errors)

    def test_invalid_property_name_rejected(self):
        item = GapRequestItem(element_system="U-Mo", properties=["bogus_prop"])
        req = GapRequest(items=[item])
        errors = validate_gap_request(req)
        assert any("bogus_prop" in e for e in errors)


class TestGapRequest:
    def test_gap_request_generates_uuid(self):
        req = GapRequest()
        assert req.request_id
        # valid uuid format
        uuid.UUID(req.request_id)  # raises ValueError if invalid
        assert req.timestamp

    def test_gap_request_serializes_to_json(self):
        req = GapRequest(items=[GapRequestItem(element_system="U-Mo", properties=["C11"])])
        s = gap_request_to_json(req)
        d = json.loads(s)
        assert d["schema_version"]
        assert d["request_id"]
        assert len(d["items"]) == 1


class TestDataSet:
    def test_data_set_status_must_be_valid(self):
        ds = DataSet(status="invalid_status")
        errors = validate_data_set(ds)
        assert any("status" in e for e in errors)

    def test_data_set_stats_defaults(self):
        stats = DataSetStats()
        assert stats.total_requested == 0
        assert stats.from_cache == 0
        assert stats.from_express == 0
        assert stats.gaps_remaining == 0


class TestRoundTrip:
    def test_from_json_roundtrip(self):
        req = GapRequest(items=[
            GapRequestItem(element_system="U-Mo", properties=["C11", "C44"]),
            GapRequestItem(element_system="U-10Zr", phase="BCC", properties=["bulk_modulus"]),
        ])
        s = gap_request_to_json(req)
        req2 = gap_request_from_json(s)
        assert req2.schema_version == req.schema_version
        assert req2.request_id == req.request_id
        assert len(req2.items) == 2
        assert req2.items[0].element_system == "U-Mo"
        assert req2.items[0].properties == ["C11", "C44"]
        assert req2.items[1].phase == "BCC"
        assert req2.items[1].properties == ["bulk_modulus"]

        # Also test DataSet roundtrip
        ds = DataSet(
            request_id=req.request_id,
            status="partial",
            stats=DataSetStats(total_requested=5, from_cache=2, from_express=1, gaps_remaining=2),
            data=[{"prop": "C11", "value": 120}],
            gaps=[{"prop": "C44", "reason": "not found"}],
        )
        s2 = data_set_to_json(ds)
        ds2 = data_set_from_json(s2)
        assert ds2.status == "partial"
        assert ds2.stats.total_requested == 5
        assert len(ds2.data) == 1
        assert len(ds2.gaps) == 1
