# Unit tests for GuessWordPuzzle behavior.


from unittest import TestCase
from src.models.puzzles.guess_word_puzzle import GuessWordPuzzle


class TestGuessWordPuzzle(TestCase):
    def setUp(self):
        self.p = GuessWordPuzzle(
            "GW-T1",
            "_ppl_",
            1,
            3,
            10,
            correct_answer="apple",
            allowed_variations=["an apple"],
        )

    # Add incorrect guesses 
    def test_add_incorrect_guess(self):
        self.p.add_incorrect_guess("mango")
        self.assertEqual(self.p.incorrect_guesses, ["mango"])

    # Check solution 
    def test_check_solution_exact_match(self):
        self.assertTrue(self.p.check_solution("apple"))

    def test_check_solution_variation_accepted(self):
        self.assertTrue(self.p.check_solution("an apple"))

    # Check solution: wrong answer 

    def test_check_solution_wrong_returns_false(self):
        self.assertFalse(self.p.check_solution("mango"))

    def test_check_solution_wrong_increments_attempts(self):
        self.p.check_solution("mango")
        self.assertEqual(self.p.attempts_made, 1)

    def test_check_solution_wrong_does_not_set_solved(self):
        self.p.check_solution("mango")
        self.assertFalse(self.p.solved)

    # Check solution state after correct answer

    def test_check_solution_sets_solved(self):
        self.p.check_solution("apple")
        self.assertTrue(self.p.solved)

    def test_check_solution_increments_attempts_on_correct(self):
        self.p.check_solution("apple")
        self.assertEqual(self.p.attempts_made, 1)

    # Check solution: invalid values
    def test_check_solution_non_string_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution(123)

    def test_check_solution_empty_string_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution("")

    def test_check_solution_returns_true_when_solved(self):
        self.p.check_solution("apple")
        self.assertTrue(self.p.check_solution("apples"))

    def test_max_attempts(self):
        p = GuessWordPuzzle(
            "GW-T1",
            "_ppl_",
            1,
            1,
            10,
            correct_answer="apple",
            allowed_variations=["an apple"],
        )

        self.assertFalse(p.check_solution("banana"))
        with self.assertRaises(ValueError):
            p.check_solution("apple")