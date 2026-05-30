"""Tests for ref_logger.py — TDD: write failing tests first."""

import json
import uuid
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from ref_logger import RefLogger


class TestStartRequest:
    def test_start_request_creates_id(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        rid = logger.start_request(items_count=5)
        # Valid uuid4
        uuid.UUID(rid, version=4)


class TestRecordCacheHit:
    def test_record_cache_hit_increments(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        logger.start_request(items_count=3)
        logger.record_cache_hit("L1")
        entry = logger._current
        assert entry["cache_hits"]["L1"] == 1


class TestRecordExpressResult:
    def test_record_express_result_increments(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        logger.start_request(items_count=3)
        logger.record_express_result()
        assert logger._current["express_results"] == 1


class TestRecordError:
    def test_record_error_appends(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        logger.start_request(items_count=3)
        logger.record_error("PDF not found")
        assert "PDF not found" in logger._current["errors"]


class TestFinishRequest:
    def test_finish_request_writes_json(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        logger.start_request(items_count=5)
        logger.finish_request(duration_seconds=1.0)
        # A file should exist under the log_dir
        files = os.listdir(tmp_path)
        assert len(files) == 1
        with open(os.path.join(tmp_path, files[0])) as f:
            data = json.load(f)
        assert isinstance(data, list)

    def test_finish_request_json_format(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        logger.start_request(items_count=5)
        logger.record_cache_hit("L1")
        logger.record_express_result()
        logger.record_error("test err")
        entry = logger.finish_request(duration_seconds=2.5, gaps_remaining=1)
        required_fields = {
            "request_id", "timestamp", "items_requested",
            "cache_hits", "express_results", "gaps_remaining",
            "duration_seconds", "slowlane_tagged_papers", "errors",
        }
        assert required_fields.issubset(entry.keys())
        assert isinstance(entry["cache_hits"], dict)
        assert isinstance(entry["errors"], list)

    def test_multiple_requests_same_day_append(self, tmp_path):
        logger = RefLogger(log_dir=str(tmp_path))
        logger.start_request(items_count=3)
        logger.finish_request(duration_seconds=1.0)

        logger2 = RefLogger(log_dir=str(tmp_path))
        logger2.start_request(items_count=2)
        logger2.finish_request(duration_seconds=1.0)

        files = os.listdir(tmp_path)
        assert len(files) == 1
        with open(os.path.join(tmp_path, files[0])) as f:
            data = json.load(f)
        assert len(data) == 2
