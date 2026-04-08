from unittest import TestCase

from src.models.puzzles.math_puzzle import MathPuzzle


class _ConcreteMathPuzzle(MathPuzzle):
    def check_solution(self, user_input):
        try:
            return float(user_input) == float(self.correct_result)
        except ValueError:
            return False


class TestMathPuzzleBase(TestCase):
    def setUp(self):
        self.p = _ConcreteMathPuzzle("M-1", "desc", 1, 1, 1, correct_result=2.5)

    def test_math_puzzle_is_abstract(self):
        with self.assertRaises(TypeError):
            MathPuzzle("M-1", "desc", 1, 1, 1, correct_result=1)

    def test_correct_result_property(self):
        self.assertEqual(self.p.correct_result, 2.5)

    def test_check_solution_correct(self):
        self.assertTrue(self.p.check_solution("2.5"))

    def test_check_solution_incorrect(self):
        self.assertFalse(self.p.check_solution("3"))

    def test_check_solution_invalid_input(self):
        self.assertFalse(self.p.check_solution("abc"))