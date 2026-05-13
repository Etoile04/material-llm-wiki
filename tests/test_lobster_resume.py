# tests/test_lobster_resume.py
import json, os, sys, time
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'skills', 'llm-wiki', 'pipeline'))
from lobster_resume import CheckpointManager

def test_checkpoint_save_and_load(tmp_path):
    cm = CheckpointManager(checkpoint_dir=str(tmp_path))
    slug = "2026_Test_Paper"
    
    cm.save(slug, step="convert", status="done", data={"raw_path": "/tmp/test.txt"})
    state = cm.load(slug)
    assert state["step"] == "convert"
    assert state["status"] == "done"
    assert state["data"]["raw_path"] == "/tmp/test.txt"

def test_checkpoint_resume(tmp_path):
    cm = CheckpointManager(checkpoint_dir=str(tmp_path))
    cm.save("paper1", "convert", "done")
    cm.save("paper2", "llm", "failed", {"retry": True})
    cm.save("paper3", "validate", "done")
    
    resumable = cm.get_resumable(["paper1", "paper2", "paper3"])
    assert len(resumable) == 1
    assert resumable[0]["slug"] == "paper2"

def test_checkpoint_cleanup(tmp_path):
    cm = CheckpointManager(checkpoint_dir=str(tmp_path))
    cm.save("old_paper", "done", "done")
    old_ts = time.time() - 48 * 3600
    state = cm.load("old_paper")
    state["unix_ts"] = old_ts
    fp = cm._filepath("old_paper")
    with open(fp, 'w') as f:
        json.dump(state, f)
    
    removed = cm.cleanup_old(24)
    assert removed == 1

def test_checkpoint_list(tmp_path):
    cm = CheckpointManager(checkpoint_dir=str(tmp_path))
    cm.save("a", "step1", "done")
    cm.save("b", "step2", "failed")
    
    cps = cm.list_checkpoints()
    assert len(cps) == 2
    assert cps[0]["slug"] == "a"
    assert cps[1]["slug"] == "b"
