#!/usr/bin/env python3
"""Unit tests for fix_missing_fields.py"""

import json
import os
import tempfile

import pytest

from fix_missing_fields import (
    fix_file,
    fix_record,
    infer_category,
    infer_name,
    infer_source_file,
    infer_value_type,
)


class TestInferValueType:
    def test_numeric_int(self):
        assert infer_value_type({"value": 42}) == "scalar"

    def test_numeric_float(self):
        assert infer_value_type({"value": 3.14}) == "scalar"

    def test_range_dict(self):
        assert infer_value_type({"value": {"min": 1, "max": 10}}) == "range"

    def test_range_dict_low_high(self):
        assert infer_value_type({"value": {"low": 1, "high": 10}}) == "range"

    def test_expression_string(self):
        assert infer_value_type({"value": "$\\frac{a}{b}$"}) == "expression"

    def test_expression_latex_frac(self):
        assert infer_value_type({"value": "y = \\frac{1}{2}"}) == "expression"

    def test_expression_latex_exp(self):
        assert infer_value_type({"value": "\\exp(x)"}) == "expression"

    def test_expression_latex_sqrt(self):
        assert infer_value_type({"value": "\\sqrt{2}"}) == "expression"

    def test_expression_latex_times(self):
        assert infer_value_type({"value": "1.0e-3 \\times 10"}) == "expression"

    def test_list_value(self):
        assert infer_value_type({"value": [1, 2, 3]}) == "list"

    def test_plain_string(self):
        assert infer_value_type({"value": "hello"}) == "scalar"

    def test_null_value(self):
        assert infer_value_type({"value": None}) == "scalar"

    def test_already_set(self):
        assert infer_value_type({"value": 42, "value_type": "range"}) == "range"

    def test_dict_no_range_keys(self):
        assert infer_value_type({"value": {"foo": "bar"}}) == "scalar"


class TestInferName:
    def test_from_property(self):
        assert infer_name({"property": "density"}) == "density"

    def test_from_description(self):
        assert infer_name({"description": "thermal conductivity"}) == "thermal conductivity"

    def test_property_over_description(self):
        assert infer_name({"property": "density", "description": "thermal conductivity"}) == "density"

    def test_fallback(self):
        assert infer_name({}) == "未命名参数"

    def test_already_set(self):
        assert infer_name({"name": "my_name", "property": "density"}) == "my_name"


class TestInferCategory:
    def test_already_set(self):
        assert infer_category({"category": "thermal"}) == "thermal"

    def test_fallback(self):
        assert infer_category({}) == "uncategorized"


class TestInferSourceFile:
    def test_from_filename_doi(self):
        record = {}
        infer_source_file(record, "10.1016_jnucmat.2024.155123.json")
        assert record["source_file"] == "10.1016_jnucmat.2024.155123"

    def test_from_filename_slug(self):
        record = {}
        infer_source_file(record, "rest-1993-cavity.json")
        assert record["source_file"] == "rest-1993-cavity"

    def test_already_set(self):
        record = {"source_file": "existing"}
        infer_source_file(record, "something.json")
        assert record["source_file"] == "existing"


class TestFixRecord:
    def test_fixes_missing_value_type(self):
        record = {"value": 42}
        fixed, changed = fix_record(record, "test.json")
        assert fixed["value_type"] == "scalar"
        assert "value_type" in changed

    def test_fixes_missing_name(self):
        record = {"property": "density", "value": 1.0}
        fixed, changed = fix_record(record, "test.json")
        assert fixed["name"] == "density"
        assert "name" in changed

    def test_no_changes_needed(self):
        record = {
            "value_type": "scalar",
            "name": "density",
            "category": "physical",
            "source_file": "test",
            "value": 1.0,
        }
        fixed, changed = fix_record(record, "test.json")
        assert changed == []

    def test_fixes_all_missing(self):
        record = {"value": 42, "property": "temp"}
        fixed, changed = fix_record(record, "paper.json")
        assert fixed["value_type"] == "scalar"
        assert fixed["name"] == "temp"
        assert fixed["category"] == "uncategorized"
        assert fixed["source_file"] == "paper"
        assert len(changed) == 4


class TestFixFile:
    def test_fix_file_writes_back(self):
        records = [
            {"value": 10, "property": "a"},
            {"value_type": "scalar", "name": "b", "category": "x", "source_file": "f", "value": 20},
        ]
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as tmp:
            json.dump(records, tmp)
            tmp_path = tmp.name

        try:
            total, fixed = fix_file(tmp_path)
            assert total == 2
            assert fixed == 1

            with open(tmp_path, "r", encoding="utf-8") as f:
                result = json.load(f)

            # First record should be fixed
            assert result[0]["value_type"] == "scalar"
            assert result[0]["name"] == "a"
            assert result[0]["category"] == "uncategorized"
            assert result[0]["source_file"] == os.path.basename(tmp_path).replace(".json", "")

            # Second record unchanged
            assert result[1]["name"] == "b"
        finally:
            os.unlink(tmp_path)
