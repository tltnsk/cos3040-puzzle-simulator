"""
This file contains the unit tests for the RiddlePuzzle class
"""

from unittest import TestCase

from src.models.puzzles.riddle_puzzle import RiddlePuzzle


class TestRiddlePuzzle(TestCase):
    def setUp(self):
        self.p = RiddlePuzzle(
            "RD-T1",
            "What has keys but cannot open locks?",
            1,
            3,
            10,
            correct_answer="piano",
            hints=["It makes music.", "It has black and white keys."],
            allowed_variations=["a piano"],
        )
    
    def test_hints_property(self):
        self.assertEqual(self.p.hints, ["It makes music.", "It has black and white keys."])

    def test_hints_used_count_property(self):
        self.assertEqual(self.p.hints_used_count, 0)

    def test_correct_answer(self):
        self.assertEqual(self.p._TextPuzzle__correct_answer, "piano")

    def test_allowed_variations(self):
        self.assertEqual(self.p._TextPuzzle__allowed_variations, ["a piano"])

    # Hints 
    def test_use_hints_first(self):
        self.assertEqual(self.p.use_hint(), "It makes music.")

    def test_use_hint_increments_count(self):
        self.p.use_hint()
        self.assertEqual(self.p.hints_used_count, 1)

    # Check solution 
    def test_check_solution_exact_match(self):
        self.assertTrue(self.p.check_solution("piano"))

    def test_check_solution_case_insensitive(self):
        self.assertTrue(self.p.check_solution("PIANO"))

    def test_check_solution_variation_accepted(self):
        self.assertTrue(self.p.check_solution("a piano"))

    # Check solution: wrong answer
    def test_check_solution_wrong(self):
        self.assertFalse(self.p.check_solution("clock"))

    # Check solution: invalid answers 
    def test_check_solution_non_string_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution(123)

    def test_check_solution_none_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution(None)

    def test_check_solution_empty_string_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution("")
        