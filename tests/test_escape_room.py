from unittest import TestCase
from unittest.mock import patch

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

    @patch("builtins.input")
    def test_show_main_menu_returns_start(self, mock_input):
        mock_input.return_value = "1"

        result = self.room.show_main_menu()

        self.assertEqual(result, "start")

    @patch("builtins.input")
    def test_choose_puzzle_mode_by_type(self, mock_input):
        mock_input.side_effect = ["1", "riddle"]

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", [], []),
            GuessWordPuzzle("G1", "_ppl_", 1, 3, 10, "apple", []),
        ]
        room = EscapeRoom(puzzles)

        result = room.choose_puzzle_mode()

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], RiddlePuzzle)

    @patch("builtins.input")
    def test_choose_puzzle_mode_by_difficulty(self, mock_input):
        mock_input.side_effect = ["2", "1"]

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", [], []),
            GuessWordPuzzle("G1", "_ppl_", 2, 3, 10, "apple", []),
        ]
        room = EscapeRoom(puzzles)

        result = room.choose_puzzle_mode()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].difficulty, 1)

    @patch("builtins.input")
    def test_choose_by_type_returns_mathing_puzzles(self, mock_input):
        mock_input.return_value = "riddle"

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", [], []),
            RiddlePuzzle("R2", "Riddle 2", 2, 3, 10, "clock", [], []),
        ]
        room = EscapeRoom(puzzles)

        result = room._choose_by_type()

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], RiddlePuzzle)
        self.assertIsInstance(result[1], RiddlePuzzle)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_choose_by_type_reprompts_after_unknown_type(self, mock_input, mock_print):
        mock_input.side_effect = ["puzzle", "riddle"]

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 2, 3, 10, "piano", [], [])
        ]
        room = EscapeRoom(puzzles)

        result = room._choose_by_type()

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], RiddlePuzzle)
        mock_print.assert_any_call("Unknown type. Choose one of: guess_word, riddle, equation, logic")

    @patch("builtins.input")
    def test_choose_by_difficulty_returns_mathing_puzzles(self, mock_input):
        mock_input.return_value = "1"

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", [], []),
            RiddlePuzzle("R2", "Riddle 2", 2, 3, 10, "clock", [], []),
        ]
        room = EscapeRoom(puzzles)

        result = room._choose_by_difficulty()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].difficulty, 1)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_choose_by_difficulty_reprompts(self, mock_input, mock_print):
        mock_input.side_effect = ["5", "2"]

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 2, 3, 10, "piano", [], [])
        ]
        room = EscapeRoom(puzzles)

        result = room._choose_by_difficulty()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].difficulty, 2)
        mock_print.assert_any_call("Please enter 1, 2, or 3.")

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

    @patch("builtins.print")
    def test_show_instructions_prints_help_text(self, mock_print):
        self.room._show_instructions()

        mock_print.assert_called_once()
        self.assertIn("--- Instructions ---", mock_print.call_args[0][0])

    @patch("builtins.input")
    def test_register_player_returns_player(self, mock_input):
        mock_input.side_effect = ["Ana", "20"]

        player = self.room.register_player()

        self.assertEqual(player.name, "Ana")
        self.assertEqual(player.age, 20)
        self.assertEqual(self.room.player, player)

    def test_update_score(self):
        self.room.player = Player("Ana", 20)
        self.room.update_score(10)
        self.assertEqual(self.room.player.score, 10)

    def test_update_score_no_player_raises(self):
        with self.assertRaises(ValueError):
            self.room.update_score(10)

    @patch("src.game.escape_room.append_result")
    def test_save_results(self, mock_append_result):
        self.room.player = Player("Ana", 20)
        self.room.update_score(10)

        self.room.save_results("test_results.json")

        mock_append_result.assert_called_once_with(
            "test_results.json",
            {
                "player_id": self.room.player.id,
                "name": "Ana",
                "score": 10,
            }
        )

    @patch("builtins.input")
    def test_play_puzzle_riddle_hint_then_correct(self, mock_input):
        self.room.player = Player("Ana", 20)
        riddle = RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", ["music"], [])
        mock_input.side_effect = ["hint", "piano"]

        result = self.room.play_puzzle(riddle)

        self.assertTrue(result)
        self.assertEqual(self.room.player.score, 10)
        self.assertEqual(riddle.hints_used_count, 1)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_play_puzzle_riddle_no_more_hints(self, mock_input, mock_print):
        self.room.player = Player("Ana", 20)
        riddle = RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", [], [])
        mock_input.side_effect = ["hint", "piano"]

        result = self.room.play_puzzle(riddle)

        self.assertTrue(result)
        mock_print.assert_any_call("No more hints.")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_play_puzzle_guess_word_shows_incorrect_guesses(self, mock_input, mock_print):
        self.room.player = Player("Ana", 20)
        puzzle = GuessWordPuzzle("G1", "_ppl_", 1, 3, 10, "apple", [])
        mock_input.side_effect = ["grape", "melon", "berry"]

        result = self.room.play_puzzle(puzzle)

        self.assertFalse(result)
        mock_print.assert_any_call("Incorrect guesses: grape")
        mock_print.assert_any_call("Incorrect guesses: grape, melon")
        mock_print.assert_any_call("Incorrect guesses: grape, melon, berry")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_play_puzzle_breaks_on_value_error(self, mock_input, mock_print):
        self.room.player = Player("Ana", 20)
        puzzle = EquationPuzzle("E1", "Equation", 1, 3, 10, "x=1", 1)
        mock_input.side_effect = [""]

        result = self.room.play_puzzle(puzzle)

        self.assertFalse(result)
        mock_print.assert_any_call("Input cannot be empty.")
        mock_print.assert_any_call("Puzzle not solved.")

    def test_start_game_exits_from_menu(self):
        with patch.object(self.room, "show_main_menu", return_value="exit"), \
             patch.object(self.room, "register_player") as mock_register, \
             patch("builtins.print") as mock_print:
            self.room.start_game()

        mock_register.assert_not_called()
        mock_print.assert_any_call("Goodbye!")

    def test_start_game_shows_instructions_then_plays_and_saves(self):
        self.room.player = Player("Ana", 20)

        with patch.object(self.room, "show_main_menu", side_effect=["instructions", "start"]), \
             patch.object(self.room, "_show_instructions") as mock_instructions, \
             patch.object(self.room, "register_player", return_value=self.room.player) as mock_register, \
             patch.object(self.room, "choose_puzzle_mode", return_value=[self.puzzles[0]]) as mock_choose, \
             patch.object(self.room, "play_puzzle", return_value=True) as mock_play, \
             patch.object(self.room, "save_results") as mock_save, \
             patch("builtins.input", return_value="n"):
            self.room.start_game("results.json")

        mock_instructions.assert_called_once()
        mock_register.assert_called_once()
        mock_choose.assert_called_once()
        mock_play.assert_called_once_with(self.puzzles[0])
        mock_save.assert_called_once_with("results.json")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_start_game_handles_empty_selection(self, mock_input, mock_print):
        self.room.player = Player("Ana", 20)
        mock_input.return_value = "n"

        with patch.object(self.room, "show_main_menu", return_value="start"), \
             patch.object(self.room, "register_player", return_value=self.room.player), \
             patch.object(self.room, "choose_puzzle_mode", return_value=[]), \
             patch.object(self.room, "play_puzzle") as mock_play:
            self.room.start_game()

        mock_play.assert_not_called()
        mock_print.assert_any_call("No puzzles to play.")