# tests/test_run_llm_ingest.py
import json, os, sys
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'skills', 'llm-wiki', 'pipeline'))
from ingest_prompt_builder import build_ingest_prompt

def test_build_ingest_prompt_basic():
    prompt = build_ingest_prompt(
        slug="2026_Test_Paper",
        raw_path="/tmp/test.md",
        wiki_root="/Users/lwj04/.openclaw/workspace/data/fuel_swelling_wiki",
        has_formulas=True
    )
    assert "2026_Test_Paper" in prompt
    assert "Key Equations" in prompt
    assert "parameters" in prompt
    assert "/tmp/test.md" in prompt

def test_build_ingest_prompt_no_formulas():
    prompt = build_ingest_prompt(
        slug="2026_NoFormula",
        raw_path="/tmp/test.md",
        wiki_root="/Users/lwj04/.openclaw/workspace/data/fuel_swelling_wiki",
        has_formulas=False
    )
    assert "Key Equations" not in prompt
