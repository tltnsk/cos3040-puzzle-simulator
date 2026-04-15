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

    def test_use_hints_second(self):
        self.p.use_hint()  # Use the first hint
        self.assertEqual(self.p.use_hint(), "It has black and white keys.")

    def test_use_hint_increments_count(self):
        self.p.use_hint()
        self.assertEqual(self.p.hints_used_count, 1)

    def test_use_hint_exhausts_hints(self):
        self.p.use_hint()
        self.p.use_hint()
        self.assertEqual(self.p.hints_used_count, 2)
        self.assertIsNone(self.p.use_hint())

    def test_use_hint_empty_list(self):
        p = RiddlePuzzle("RD-T2", "?", 1, 3, 10, correct_answer="piano", hints=[], allowed_variations=[])
        self.assertIsNone(p.use_hint())

    # Check solution 

    def test_check_solution_exact_match(self):
        self.assertTrue(self.p.check_solution("piano"))

    def test_check_solution_case_insensitive(self):
        self.assertTrue(self.p.check_solution("PIANO"))

    def test_check_solution_strips_whitespace(self):
        self.assertTrue(self.p.check_solution("  piano  "))

    def test_check_solution_variation_accepted(self):
        self.assertTrue(self.p.check_solution("a piano"))

    def test_check_solution_variation_case_insensitive(self):
        self.assertTrue(self.p.check_solution("A Piano"))

    def test_check_solution_returns_true_if_already_solved(self):
        self.p.check_solution("piano")   
        self.assertTrue(self.p.check_solution("wrong answer"))  
    
    # Check solution: wrong answer
    def test_check_solution_wrong(self):
        self.assertFalse(self.p.check_solution("clock"))

    def test_check_solution_wrong_increments_attempts(self):
        self.p.check_solution("clock")
        self.assertEqual(self.p.attempts_made, 1)
        self.assertEqual(self.p._Puzzle__attempts_made, 1)

    def test_check_solution_wrong_does_not_set_solved(self):
        self.p.check_solution("clock")
        self.assertFalse(self.p.solved)

    
    # Check solution state after correct answer has been provided 
    def test_check_solution_sets_solved(self):
        self.p.check_solution("piano")
        self.assertTrue(self.p.solved)
        self.assertTrue(self.p._Puzzle__is_solved)

    def test_check_solution_increments_attempts_on_correct(self):
        self.p.check_solution("piano")
        self.assertEqual(self.p.attempts_made, 1)

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

    def test_check_solution_whitespace_only_raises(self):
        with self.assertRaises(ValueError):
            self.p.check_solution("   ")
        
    # Check max attempts
    def test_max_attempts(self):
        p = RiddlePuzzle(
            "RD-T4",
            "What has keys but cannot open locks?",
            1,
            1,
            10,
            correct_answer="piano",
            hints=[],
            allowed_variations=[],
        )

        self.assertFalse(p.check_solution("clock"))
        self.assertEqual(p.attempts_made, 1)
        self.assertEqual(p._Puzzle__attempts_made, 1)

        with self.assertRaises(ValueError):
            p.check_solution("piano")

