from unittest import TestCase

from src.game.escape_room import EscapeRoom
from src.models.player import Player
from src.models.puzzles.riddle_puzzle import RiddlePuzzle
from src.models.puzzles.guess_word_puzzle import GuessWordPuzzle
from src.models.puzzles.logic_puzzle import LogicPuzzle
from src.models.puzzles.equation_puzzle import EquationPuzzle

class TestEscapeRoom(TestCase):
    def setUp(self):
        self.puzzles = [
            RiddlePuzzle("RD-1", "What has keys but can't open locks?", 1, 3, 10, correct_answer="piano", hints=[], allowed_variations=[]),
            GuessWordPuzzle("GW-1", "_ppl_", 1, 3, 10, correct_answer="apple", allowed_variations=[]),
            LogicPuzzle("LP-1", "How many truth values exist?", 1, 2, 10, correct_result=2, explanation="True and false."),
            EquationPuzzle("EQ-1", "Solve: x + 2 = 3", 1, 3, 19, equation="x + 2 = 3", tolerance=1e-9, correct_result=1)
        ]

        self.room = EscapeRoom(self.puzzles)

    def test_puzzles_property(self):
        self.assertEqual(len(self.room.puzzles), len(self.puzzles))

    def test_puzzles_setter(self):
        with self.assertRaises(ValueError):
            self.room.puzzles = None

        self.puzzles = [
            RiddlePuzzle("R-1", "What has keys but can't open locks?", 1, 3, 10, correct_answer="piano", hints=[], allowed_variations=[]),
            GuessWordPuzzle("G-1", "_ppl_", 1, 3, 10, correct_answer="apple", allowed_variations=[]),
            LogicPuzzle("L-1", "How many truth values exist?", 1, 2, 10, correct_result=2, explanation="True and false."),
            EquationPuzzle("E-1", "Solve: x + 2 = 3", 1, 3, 19, equation="x + 2 = 3", tolerance=1e-9, correct_result=1)
        ]
        self.room.puzzles = self.puzzles
        self.assertEqual(self.room.puzzles, self.puzzles)   
    
    def test_player_default_none(self):
        self.assertIsNone(self.room.player)

    def test_player_setter(self):
        player = Player("Ana", 20)
        self.room.player = player
        self.assertEqual(self.room.player, player)

    def test_player_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.room.player = "Invalid Player"

    def test_filter_puzzles_by_type_riddle(self):
        result = self.room.filter_puzzles_by_type("riddle")
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], RiddlePuzzle)

    def test_filter_puzzles_by_type_guess_word(self):
        result = self.room.filter_puzzles_by_type("guess_word")
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], GuessWordPuzzle)

    def test_filter_puzzles_by_type_unknown_raises(self):
        with self.assertRaises(ValueError):
            self.room.filter_puzzles_by_type("unknown")

    def test_filter_puzzles_by_difficulty(self):
        result = self.room.filter_puzzles_by_difficulty(1)
        self.assertEqual(len(result), 4)

    def test_filter_puzzles_by_difficulty_no_match(self):
        result = self.room.filter_puzzles_by_difficulty(3)
        self.assertEqual(result, [])

    def test_update_score(self):
        self.room.player = Player("Ana", 20)
        self.room.update_score(10)
        self.assertEqual(self.room.player.score, 10)

    def test_update_score_no_player_raises(self):
        with self.assertRaises(ValueError):
            self.room.update_score(10)

    def test_save_results_no_player_raises(self):
        with self.assertRaises(ValueError):
            self.room.save_results("results.json")

    def test_save_results(self):
        self.room.player = Player("Ana", 20)
        self.room.update_score(10)
        self.room.save_results("test_results.json")
        import json
        with open("test_results.json") as f:
            data = json.load(f)
        self.assertEqual(data[-1]["name"], "Ana")
        self.assertEqual(data[-1]["score"], 10)