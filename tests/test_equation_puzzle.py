from unittest import TestCase


from src.models.puzzles.equation_puzzle import EquationPuzzle


class TestEquationPuzzle(TestCase):
    def setUp(self):
        self.p = EquationPuzzle(
            "EQ-T1",
            "Solve: x = 3",
            1,
            3,
            10,
            equation="x = 3",
            tolerance=1e-9,
            correct_result=3,
        )

    def test_equation(self):
        self.assertEqual(self.p.equation, "x = 3")

    def test_tolerance(self):
        self.assertEqual(self.p.tolerance, 1e-9)

    # Check solution: correct result
    def test_check_solution_correct_result(self):
        self.assertTrue(self.p.check_solution("3"))

    # Check solution with tolerance
    def test_check_solution_with_tolerance(self):
        self.assertTrue(self.p.check_solution("3.000000001"))

    # Check solution: incorrect result
    def test_check_solution_incorrect_result(self):
        self.assertFalse(self.p.check_solution("4"))

    def test_check_solution_non_integer(self):
        self.assertFalse(self.p.check_solution("four"))

    def test_check_solution_empty_string(self):
        with self.assertRaises(Exception):
            self.p.check_solution("")

    def test_check_solution_non_string(self):
        with self.assertRaises(ValueError):
            self.p.check_solution(123)

    # Check solution state after correct result has been provided
    def test_check_solution_correct_sets_solved(self):
        self.p.check_solution("3")
        self.assertTrue(self.p.solved)