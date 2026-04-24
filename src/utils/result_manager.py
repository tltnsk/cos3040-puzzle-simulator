"""
Result storage helpers.

Loads, saves, and appends game results stored as JSON lists.
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
    """
    Write the full results list to a JSON file.

    Parameters
    ----------
    file_path : str
        Path to the JSON results file.
    results : list
        Results to save.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


def append_result(file_path, result):
    """
    Load the results, add one result, and save the updated list.

    Parameters
    ----------
    file_path : str
        Path to the JSON results file.
    result : dict
        Result entry to append.
    """
    results = load_results(file_path)
    results.append(result)
    save_results(file_path, results)