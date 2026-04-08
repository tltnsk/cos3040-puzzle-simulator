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
            RiddlePuzzle("RD-1", "What has keys but can't open locks?", 1, 3, 10, correct_answer="piano", hint=[], allowed_variations=[]),
            GuessWordPuzzle("GW-1", "_ppl_", 1, 3, 10, correct_answer="apple", allowed_variations=[]),
            LogicPuzzle("LP-1", "How many truth values exist?", 1, 2, 10, correct_result=2, explanation="True and false."),
            EquationPuzzle("EQ-1", "Solve: x + 2 = 3", 1, 3, 19, equation="x + 2 = 3", tolerance=1e-9, correct_result=1)
        ]

        self.room = EscapeRoom(self.puzzles)

    def test_puzzles_property(self):
        self.assertEqual(self.room.puzzles, self.puzzles)

    def test_puzzles_setter(self):
        with self.assertRaises(ValueError):
            self.room.puzzles = None

        self.puzzles = [
            RiddlePuzzle("R-1", "What has keys but can't open locks?", 1, 3, 10, correct_answer="piano", hint=[], allowed_variations=[]),
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