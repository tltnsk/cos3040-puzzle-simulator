from unittest import TestCase

from src.models.puzzles.text_puzzle import TextPuzzle


class _ConcreteTextPuzzle(TextPuzzle):
    def check_solution(self, user_input):
        return user_input.strip().lower() == self.correct_answer.strip().lower()

class TestTextPuzzleBase(TestCase):
    def setUp(self):
        self.p = _ConcreteTextPuzzle(
            "T-1",
            "desc",
            1,
            1,
            1,
            correct_answer="Hello",
            allowed_variations=["hi", "hey"],
        )

    def test_text_puzzle_is_abstract(self):
        with self.assertRaises(TypeError):
            TextPuzzle("T-1", "desc", 1, 1, 1, correct_answer="a")

    def test_correct_answer_property(self):
        self.assertEqual(self.p.correct_answer, "Hello")

    def test_allowed_variations_property(self):
        self.assertEqual(self.p.allowed_variations, ["hi", "hey"])

    def test_allowed_variations_default_to_empty_list(self):
        p = _ConcreteTextPuzzle("T-2", "desc", 1, 1, 1, correct_answer="Hello")
        self.assertEqual(p.allowed_variations, [])
        self.assertEqual(p._TextPuzzle__allowed_variations, [])