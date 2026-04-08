import unittest

from src.models.puzzles.logic_puzzle import LogicPuzzle


class TestLogicPuzzle(unittest.TestCase):
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

    def test_check_solution_empty_string(self):
        with self.assertRaises(Exception):
            self.p.check_solution("")

    def test_check_solution_whitespace_only(self):
        with self.assertRaises(Exception):
            self.p.check_solution("   ")

    def test_check_solution_wrong_increments_attempts(self):
        self.p.check_solution("3")
        self.assertEqual(self.p.attempts_made, 1)

    def test_check_solution_wrong_does_not_set_solved(self):
        self.p.check_solution("3")
        self.assertFalse(self.p.solved)

    # Check solution state after correct answer has been provided
    def test_check_solution_correct_sets_solved(self):
        self.p.check_solution("2")
        self.assertTrue(self.p.solved)

    def test_check_solution_correct_increments_attempts(self):
        self.p.check_solution("2")
        self.assertEqual(self.p.attempts_made, 1)

    # Check solution: max attempts:
    def test_max_attempts(self):
        p = LogicPuzzle(
            "LG-T2",
            "What is 1 + 1?",
            1,
            1,
            10,
            correct_result=2,
            explanation="1 + 1 equals 2.",
        )

        self.assertFalse(p.check_solution("3"))
        self.assertEqual(p.attempts_made, 1)

        with self.assertRaises(Exception):
            p.check_solution("2")