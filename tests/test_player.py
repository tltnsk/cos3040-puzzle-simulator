from unittest import TestCase

from src.models.player import Player

class TestPlayer(TestCase):
    def setUp(self):
        Player._next_id = 0 
        self.p = Player("Ana", 20)

    def test_player_name(self):
        self.assertEqual(self.p.name, "Ana")    

    def test_player_age(self):
        self.assertEqual(self.p.age, 20)

    def test_player_id(self):
        self.assertIsInstance(self.p.id, int)
        self.assertEqual(self.p.id, 1)

    def test_name_setter(self):
        for invalid in ("", "   ", 123, None):
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

    def test_add_score_accumulates(self):
        self.p.add_score(10)
        self.p.add_score(5)
        self.assertEqual(self.p.score, 15)

    def test_add_score_zero(self):
        self.p.add_score(0)
        self.assertEqual(self.p.score, 0)

    def test_add_score_negative(self):
        with self.assertRaises(ValueError):
            self.p.add_score(-10)   

    def test_add_score_non_integer(self):
        with self.assertRaises(ValueError):
            self.p.add_score("ten")

    def test_reset_score(self):
        self.p.add_score(10)
        self.p.reset_score()
        self.assertEqual(self.p.score, 0)

    def test_str_format(self):
        self.assertEqual(str(self.p), "Ana (ID: 1, Age: 20, Score: 0)")

