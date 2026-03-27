"""
Result manager helpers.

Loads the results from the file and also writes results to the file.
"""

import json


def load_results(file_path):
    """
    Load results from a JSON file.

    The file is expected to contain a JSON list. If the file does not exist,
    is empty, or is invalid JSON, this returns an empty list.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_results(file_path, results):
    """Write the full results list to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


def append_result(file_path, result):
    """
    Load the results, add the current result to them and save the results to the file.
    """
    results = load_results(file_path)
    results.append(result)
    save_results(file_path, results)
