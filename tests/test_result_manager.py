# Unit tests for result loading and persistence helpers.

import json
from unittest import TestCase

from src.utils.result_manager import load_results, save_results, append_result


class TestResultManager(TestCase):
    def test_load_results_valid_file(self):
        with open("test_results.json", "w") as f:
            json.dump([{"id": 1, "result": "pass"}], f)
        results = load_results("test_results.json")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], 1)
        self.assertEqual(results[0]["result"], "pass")

    def test_load_results_json_error(self):
        with open("test_result.json", "w") as f:
            f.write("invalid json{{{}}}")
        results = load_results("test_result.json")
        self.assertEqual(results, [])

    def test_load_results_file_not_found(self):
        results = load_results("file_not_exist.json")
        self.assertEqual(results, [])

    def test_save_results(self):
        results = [{"id": 1, "result": "pass"}]
        save_results("test_results.json", results)
        loaded_results = load_results("test_results.json")
        self.assertEqual(loaded_results, results)

    def test_append_result(self):
        with open("test_results.json", "w") as f:
            json.dump([], f)
        append_result("test_results.json", {"id": 2, "result": "fail"})
        results = load_results("test_results.json")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], 2)
