"""
This file contains the unit tests for the LogicPuzzle
"""

from unittest import TestCase

from src.models.puzzles.logic_puzzle import LogicPuzzle


class TestLogicPuzzle(TestCase):
    def setUp(self):
        self.p = LogicPuzzle(
            "LG-T1",
            "How many truth values exist?",
            1,
            2,
            10,
            correct_result=2,
            explanation="True and false.",
        )

    def test_explanation_property(self):
        self.assertEqual(self.p.explanation, "True and false.")

    # Check solution: correct result
    def test_check_solution_correct_result(self):
        self.assertTrue(self.p.check_solution("2"))

    # Check solution: incorrect result
    def test_check_solution_incorrect_result(self):
        self.assertFalse(self.p.check_solution("3"))

    def test_check_solution_non_integer(self):
        self.assertFalse(self.p.check_solution("two"))

    def test_check_solution_non_string(self):
        with self.assertRaises(ValueError):
            self.p.check_solution(123)

    def test_check_solution_empty_string(self):
        with self.assertRaises(Exception):
            self.p.check_solution("")
