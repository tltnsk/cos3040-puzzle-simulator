# Unit tests for the Player model.


from unittest import TestCase

from src.models.player import Player


class TestPlayer(TestCase):
    def setUp(self):
        self.p = Player("Ana", 20)

    def test_player_name(self):
        self.assertEqual(self.p.name, "Ana")

    def test_player_age(self):
        self.assertEqual(self.p.age, 20)

    def test_name_setter(self):
        for invalid in ("", "   ", "abc", 123, None):
            with self.assertRaises(ValueError):
                self.p.name = invalid
        self.p.name = "Joana"
        self.assertEqual(self.p.name, "Joana")

    def test_age_setter(self):
        for invalid in ("", "   ", -1, None):
            with self.assertRaises(ValueError):
                self.p.age = invalid
        self.p.age = 30
        self.assertEqual(self.p.age, 30)

    def test_add_score(self):
        self.p.add_score(10)
        self.assertEqual(self.p.score, 10)

    def test_add_score_negative(self):
        with self.assertRaises(ValueError):
            self.p.add_score(-10)

    def test_reset_score(self):
        self.p.add_score(10)
        self.p.reset_score()
        self.assertEqual(self.p.score, 0)

    def test_str_format(self):
        self.assertEqual(str(self.p), "Ana (Age: 20, Score: 0)")
