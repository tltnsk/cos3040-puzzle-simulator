"""
Puzzle loading utilities.

Reads puzzle definitions from JSON, validates required fields, and creates the
appropriate puzzle objects for the game.
"""

import json

from src.models.puzzles.equation_puzzle import EquationPuzzle
from src.models.puzzles.guess_word_puzzle import GuessWordPuzzle
from src.models.puzzles.logic_puzzle import LogicPuzzle
from src.models.puzzles.riddle_puzzle import RiddlePuzzle


def _require_field(entry, field_name):
    """
    Return a required field from a puzzle JSON entry.

    Parameters
    ----------
    entry : dict
        The JSON entry to check.
    field_name : str
        The name of the field to check.

    Returns
    ----------
    object
        The value of the field.

    Raises
    ----------
    KeyError
        If the field is not found in the entry.
    """
    if field_name not in entry:
        raise KeyError(
            f"Missing required field '{field_name}' in puzzle entry: {entry}"
        )
    return entry[field_name]


def load_puzzles(file_path):
    """
    Load puzzles from a JSON file and return a list of puzzle objects.

    Expected JSON structure: a list of objects, each with a 'type' field
    and the fields required by that puzzle type.

    Parameters
    ----------
    file_path : str
        Path to the JSON file containing puzzle definitions.

    Returns
    -------
    list
        A list of instantiated puzzle objects.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Puzzle data must be a list of puzzle objects.")

    puzzles = []

    for entry in data:
        puzzle_type = _require_field(entry, "type").strip().lower()
        puzzle_id = _require_field(entry, "id")
        description = _require_field(entry, "description")
        difficulty = _require_field(entry, "difficulty")
        max_attempts = _require_field(entry, "max_attempts")
        points = _require_field(entry, "points")

        if puzzle_type == "guess_word":
            puzzles.append(
                GuessWordPuzzle(
                    puzzle_id,
                    description,
                    difficulty,
                    max_attempts,
                    points,
                    _require_field(entry, "correct_answer"),
                    entry.get("allowed_variations", []),
                )
            )
        elif puzzle_type == "riddle":
            puzzles.append(
                RiddlePuzzle(
                    puzzle_id,
                    description,
                    difficulty,
                    max_attempts,
                    points,
                    _require_field(entry, "correct_answer"),
                    entry.get("hints", []),
                    entry.get("allowed_variations", []),
                )
            )
        elif puzzle_type == "equation":
            puzzles.append(
                EquationPuzzle(
                    puzzle_id,
                    description,
                    difficulty,
                    max_attempts,
                    points,
                    equation=_require_field(entry, "equation_expression"),
                    correct_result=_require_field(entry, "correct_result"),
                )
            )
        elif puzzle_type == "logic":
            puzzles.append(
                LogicPuzzle(
                    puzzle_id,
                    description,
                    difficulty,
                    max_attempts,
                    points,
                    _require_field(entry, "correct_result"),
                    _require_field(entry, "explanation"),
                )
            )
        else:
            raise ValueError(
                f"Unknown puzzle type '{puzzle_type}' in entry: {entry}"
            )

    return puzzles