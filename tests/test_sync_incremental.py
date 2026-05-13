# tests/test_sync_incremental.py
import json, os, sys, time
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))
from sync_incremental import detect_new_params, build_upsert_batch


def test_detect_new_params(tmp_path):
    params_dir = tmp_path / "params"
    params_dir.mkdir()
    (params_dir / "test.json").write_text(json.dumps([{"id": "test_001", "name": "test"}]))

    result = detect_new_params(str(params_dir))
    assert len(result) == 1


def test_detect_no_new_params(tmp_path):
    params_dir = tmp_path / "params"
    params_dir.mkdir()
    (params_dir / "test.json").write_text(json.dumps([{"id": "test_001"}]))

    # Sync at current time (files are older)
    ts = time.time()
    result = detect_new_params(str(params_dir), ts)
    assert len(result) == 0


def test_build_upsert_batch():
    params = [{"id": str(i), "name": f"P{i}"} for i in range(250)]
    batches = build_upsert_batch(params, batch_size=100)
    assert len(batches) == 3
    assert len(batches[0]) == 100
    assert len(batches[1]) == 100
    assert len(batches[2]) == 50


def test_build_upsert_batch_small():
    params = [{"id": "1"}]
    batches = build_upsert_batch(params, batch_size=100)
    assert len(batches) == 1
    assert len(batches[0]) == 1


def test_detect_new_params_empty_dir(tmp_path):
    params_dir = tmp_path / "params"
    params_dir.mkdir()
    result = detect_new_params(str(params_dir))
    assert len(result) == 0
