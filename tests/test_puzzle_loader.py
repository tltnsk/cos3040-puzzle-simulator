import json
from unittest import TestCase

from src.utils.puzzle_loader import load_puzzles

class TestLoadPuzzles(TestCase):
    def test_load_guess_word_puzzle(self):
        with open("test_puzzles.json", "w") as f:
            json.dump([{
                "type": "guess_word", "id": "GW-1", "description": "_ p p l _",
                "difficulty": 1, "max_attempts": 3, "points": 10,
                "correct_answer": "apple"
            }], f)
        puzzles = load_puzzles("test_puzzles.json")
        self.assertEqual(len(puzzles), 1)

    def test_load_riddle_puzzle(self):
        with open("test_puzzles.json", "w") as f:
            json.dump([{
                "type": "riddle", "id": "RD-1", "description": "What has keys?",
                "difficulty": 1, "max_attempts": 3, "points": 10,
                "correct_answer": "piano", "hints": []
            }], f)
        puzzles = load_puzzles("test_puzzles.json")
        self.assertEqual(len(puzzles), 1)

    def test_load_logic_puzzle(self):
        with open("test_puzzles.json", "w") as f:
            json.dump([{
                "type": "logic", "id": "LG-1", "description": "If A > B and B > C, who is smallest?",
                "difficulty": 1, "max_attempts": 3, "points": 10,
                "correct_result": "C", "explanation": "C is smaller than B which is smaller than A."
            }], f)
        puzzles = load_puzzles("test_puzzles.json")
        self.assertEqual(len(puzzles), 1)

    def test_load_equation_puzzle(self):
        with open("test_puzzles.json", "w") as f:
            json.dump([{
                "type": "equation", "id": "EQ-1", "description": "Solve: x = 3",
                "difficulty": 1, "max_attempts": 3, "points": 10,
                "equation_expression": "x = 3", "tolerance": 1e-9, "correct_result": 3
            }], f)
        puzzles = load_puzzles("test_puzzles.json")
        self.assertEqual(len(puzzles), 1)

    def test_unknown_type_raises(self):
        with open("test_puzzles.json", "w") as f:
            json.dump([{
                "type": "unknown", "id": "X-1", "description": "?",
                "difficulty": 1, "max_attempts": 3, "points": 10
            }], f)
        with self.assertRaises(ValueError):
            load_puzzles("test_puzzles.json")

    def test_missing_field_raises(self):
        with open("test_puzzles.json", "w") as f:
            json.dump([{"type": "riddle", "id": "RD-1"}], f)
        with self.assertRaises(KeyError):
            load_puzzles("test_puzzles.json")

    def test_data_not_list_raises(self):
        with open("test_puzzles.json", "w") as f:
            json.dump({"type": "riddle"}, f)
        with self.assertRaises(ValueError):
            load_puzzles("test_puzzles.json")