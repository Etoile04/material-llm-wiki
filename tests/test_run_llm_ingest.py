# tests/test_run_llm_ingest.py
import json, os, sys, subprocess
import pytest

SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'skills', 'llm-wiki', 'scripts', 'run_llm_ingest.py'
)


def test_script_exists():
    """Verify run_llm_ingest.py exists at expected path."""
    assert os.path.isfile(SCRIPT_PATH), f"Script not found: {SCRIPT_PATH}"


def test_script_importable():
    """Verify the script is syntactically valid Python."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("run_llm_ingest", SCRIPT_PATH)
    assert spec is not None
    # Just verify it parses (don't execute main)
    module = importlib.util.module_from_spec(spec)
    # Don't exec the module fully since it has side effects on import
    with open(SCRIPT_PATH) as f:
        source = f.read()
    compile(source, SCRIPT_PATH, 'exec')  # Will raise SyntaxError if invalid
