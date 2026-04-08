import unittest


from src.models.puzzles.equation_puzzle import EquationPuzzle


class TestEquationPuzzle(unittest.TestCase):
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

    def test_check_solution_whitespace_only(self):
        with self.assertRaises(Exception):
            self.p.check_solution("   ")

    def test_check_solution_wrong_increments_attempts(self):
        self.p.check_solution("4")
        self.assertEqual(self.p.attempts_made, 1)   

    def test_check_solution_wrong_does_not_set_solved(self):
        self.p.check_solution("4")
        self.assertFalse(self.p.solved)

    # Check solution state after correct result has been provided
    def test_check_solution_correct_sets_solved(self):
        self.p.check_solution("3")
        self.assertTrue(self.p.solved)

    def test_check_solution_correct_increments_attempts(self):
        self.p.check_solution("3")
        self.assertEqual(self.p.attempts_made, 1)

    # Check solution: max attempts
    def test_max_attempts(self):
        p = EquationPuzzle(
            "EQ-T1",
            "Solve: x = 3",
            1,
            1,
            10,
            equation="x = 3",
            tolerance=1e-9,
            correct_result=3,
        )

        self.assertFalse(p.check_solution("4"))
        self.assertEqual(p.attempts_made, 1)

        with self.assertRaises(Exception):
            p.check_solution("4")   