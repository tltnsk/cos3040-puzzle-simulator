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


    def test_incorrect_guesses_initially_empty(self):
        self.assertEqual(self.p.incorrect_guesses, [])

    # Add incorrect guesses 

    def test_add_incorrect_guess(self):
        self.p.add_incorrect_guess("mango")
        self.assertEqual(self.p.incorrect_guesses, ["mango"])

    def test_add_multiple_incorrect_guesses(self):
        self.p.add_incorrect_guess("mango")
        self.p.add_incorrect_guess("grape")
        self.assertEqual(self.p.incorrect_guesses, ["mango", "grape"])

    # Check solution 

    def test_check_solution_exact_match(self):
        self.assertTrue(self.p.check_solution("apple"))

    def test_check_solution_case_insensitive(self):
        self.assertTrue(self.p.check_solution("APPLE"))

    def test_check_solution_strips_whitespace(self):
        self.assertTrue(self.p.check_solution("  apple  "))

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

    def test_check_solution_wrong_adds_to_incorrect_guesses(self):
        self.p.check_solution("mango")
        self.assertIn("mango", self.p.incorrect_guesses)

    def test_check_solution_correct_does_not_add_to_incorrect_guesses(self):
        self.p.check_solution("apple")
        self.assertEqual(self.p.incorrect_guesses, [])

    # Check solution state after correct answer

    def test_check_solution_sets_solved(self):
        self.p.check_solution("apple")
        self.assertTrue(self.p.solved)

    def test_check_solution_increments_attempts_on_correct(self):
        self.p.check_solution("apple")
        self.assertEqual(self.p.attempts_made, 1)

    # Check solution: already solved
    def test_check_solution_returns_true_when_already_solved(self):
        self.p.check_solution("apple")
        self.assertTrue(self.p.check_solution("anything"))

    def test_check_solution_does_not_increment_attempts_when_already_solved(self):
        self.p.check_solution("apple")
        self.p.check_solution("anything")
        self.assertEqual(self.p.attempts_made, 1)

    # Check solution: invalid values

    def test_check_solution_non_string_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution(123)

    def test_check_solution_empty_string_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution("")

    def test_check_solution_whitespace_only_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution("   ")

    # Check solution: max attempts 

    def test_check_solution_raises_at_max_attempts(self):
        p = GuessWordPuzzle("GW-T2", "?", 1, 1, 10, correct_answer="apple", allowed_variations=[])
        p.check_solution("mango")
        with self.assertRaises(ValueError):
            p.check_solution("apple")