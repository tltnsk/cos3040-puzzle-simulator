from unittest import TestCase

from src.models.puzzles.puzzle import Puzzle

# Small subclass so I can actually create a Puzzle object and 
# test the parent class  
class _ConcretePuzzle(Puzzle):
    def check_solution(self, solution):
        return bool(solution)

class TestPuzzle(TestCase):
    def setUp(self):
        # Valid puzzle instance 
        self.p = _ConcretePuzzle("P-1", "A test puzzle", 2, 3, 10)

    def test_puzzle_is_abstract(self):
        with self.assertRaises(TypeError):
            Puzzle("P-1", "desc", 1, 1, 1)

    def test_id_property(self):
        self.assertEqual(self.p.id, "P-1")

    def test_description_property(self):
        self.assertEqual(self.p.description, "A test puzzle")

    def test_difficulty_property(self):
        self.assertEqual(self.p.difficulty, 2)

    def test_max_attempts_property(self):
        self.assertEqual(self.p.max_attempts, 3)

    def test_attempts_made_property(self):
        self.assertEqual(self.p.attempts_made, 0)

    def test_points_property(self):
        self.assertEqual(self.p.points, 10)

    def test_solved_property(self):
        self.assertFalse(self.p.solved)

    def test_description_setter(self):
        self.p.description = "New description"
        self.assertEqual(self.p.description, "New description")

    def test_difficulty_setter(self):
        for invalid in (0, 4, -1, "1"):
            with self.assertRaises(ValueError):
                self.p.difficulty = invalid

        self.p.difficulty = 3
        self.assertEqual(self.p.difficulty, 3)

    def test_max_attempts_setter(self):
        with self.assertRaises(ValueError):
            self.p.max_attempts = -1

        self.p.max_attempts = 5
        self.assertEqual(self.p.max_attempts, 5)

    def test_attempts_made_setter(self):
        self.p.attempts_made = 2
        self.assertEqual(self.p.attempts_made, 2)

        with self.assertRaises(ValueError):
            self.p.attempts_made = -1

        with self.assertRaises(ValueError):
            self.p.attempts_made = 4

    def test_points_setter(self):
        with self.assertRaises(ValueError):
            self.p.points = -5

        self.p.points = 15
        self.assertEqual(self.p.points, 15)

    def test_solved_setter(self):
        self.p.solved = True
        self.assertTrue(self.p.solved)

    def test_str_format(self):
        self.assertEqual(str(self.p), "Puzzle P-1: A test puzzle (Difficulty 2)")

    def test_comparison_lt(self):
        a = _ConcretePuzzle("P-1", "desc", 1, 1, 1)
        b = _ConcretePuzzle("P-2", "desc", 3, 1, 1)

        self.assertTrue(a < b)
        self.assertFalse(b < a)
        self.assertFalse(a < "not a puzzle")

    def test_comparison_eq(self):
        a = _ConcretePuzzle("P-1", "desc", 1, 1, 1)
        b = _ConcretePuzzle("P-2", "desc", 3, 1, 1)
        c = _ConcretePuzzle("P-1", "desc", 2, 1, 1)

        self.assertTrue(a == c)
        self.assertFalse(a == b)
        self.assertFalse(a == "not a puzzle")
