# Unit tests for EscapeRoom game flow and helpers.


from unittest import TestCase
from unittest.mock import patch

from src.game.escape_room import EscapeRoom
from src.models.player import Player
from src.models.puzzles.equation_puzzle import EquationPuzzle
from src.models.puzzles.guess_word_puzzle import GuessWordPuzzle
from src.models.puzzles.logic_puzzle import LogicPuzzle
from src.models.puzzles.riddle_puzzle import RiddlePuzzle


class TestEscapeRoom(TestCase):
    def setUp(self):
        self.puzzles = [
            RiddlePuzzle(
                "RD-1",
                "What has keys but can't open locks?",
                1,
                3,
                10,
                correct_answer="piano",
                hints=[],
                allowed_variations=[],
            ),
            GuessWordPuzzle(
                "GW-1",
                "_ppl_",
                1,
                3,
                10,
                correct_answer="apple",
                allowed_variations=[],
            ),
            LogicPuzzle(
                "LP-1",
                "How many truth values exist?",
                1,
                2,
                10,
                correct_result=2,
                explanation="True and false.",
            ),
            EquationPuzzle(
                "EQ-1",
                "Solve: x + 2 = 3",
                1,
                3,
                19,
                equation="x + 2 = 3",
                tolerance=1e-9,
                correct_result=1,
            ),
        ]

        self.room = EscapeRoom(self.puzzles)

    def test_puzzles_property(self):
        self.assertEqual(len(self.room.puzzles), len(self.puzzles))

    def test_puzzles_setter(self):
        with self.assertRaises(ValueError):
            self.room.puzzles = None

        self.puzzles = [
            RiddlePuzzle(
                "R-1",
                "What has keys but can't open locks?",
                1,
                3,
                10,
                correct_answer="piano",
                hints=[],
                allowed_variations=[],
            ),
            GuessWordPuzzle(
                "G-1",
                "_ppl_",
                1,
                3,
                10,
                correct_answer="apple",
                allowed_variations=[],
            ),
            LogicPuzzle(
                "L-1",
                "How many truth values exist?",
                1,
                2,
                10,
                correct_result=2,
                explanation="True and false.",
            ),
            EquationPuzzle(
                "E-1",
                "Solve: x + 2 = 3",
                1,
                3,
                19,
                equation="x + 2 = 3",
                tolerance=1e-9,
                correct_result=1,
            ),
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
    def test_show_main_menu_returns_instructions(self, mock_input):
        mock_input.return_value = "2"

        result = self.room.show_main_menu()

        self.assertEqual(result, "instructions")

    @patch("builtins.input")
    def test_show_main_menu_returns_exit(self, mock_input):
        mock_input.return_value = "3"

        result = self.room.show_main_menu()

        self.assertEqual(result, "exit")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_show_main_menu_reprompts(self, mock_input, mock_print):
        mock_input.side_effect = ["4", "1"]

        result = self.room.show_main_menu()

        self.assertEqual(result, "start")
        mock_print.assert_any_call("Please enter 1, 2, or 3.")

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
    def test_choose_puzzle_mode_invalid(self, mock_input):
        mock_input.side_effect = ["7", "2", "1"]
        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", [], []),
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
    def test_choose_by_type_reprompts_after_unknown_type(
        self,
        mock_input,
        mock_print,
    ):
        mock_input.side_effect = ["puzzle", "riddle"]

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 2, 3, 10, "piano", [], []),
        ]
        room = EscapeRoom(puzzles)

        result = room._choose_by_type()

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], RiddlePuzzle)
        mock_print.assert_any_call(
            "Unknown type. Choose one of: guess_word, riddle, equation, logic"
        )

    @patch("builtins.print")
    @patch("builtins.input")
    def test_choose_by_type_reprompts_when_no_puzzles_for_that_type(
        self,
        mock_input,
        mock_print,
    ):
        mock_input.side_effect = ["logic", "riddle"]

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", [], []),
            GuessWordPuzzle(
                "G1",
                "_ppl_",
                1,
                3,
                10,
                correct_answer="apple",
                allowed_variations=[],
            ),
        ]

        room = EscapeRoom(puzzles)

        result = room._choose_by_type()

        mock_print.assert_any_call(
            "Such type of puzzle does not exist. Try another."
        )

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], RiddlePuzzle)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_choose_by_difficulty_reprompts_when_no_puzzles_for_that_level(
        self,
        mock_input,
        mock_print,
    ):
        mock_input.side_effect = ["3", "1"]

        puzzles = [
            RiddlePuzzle("R1", "Riddle 1", 1, 3, 10, "piano", [], []),
            RiddlePuzzle("R2", "Riddle 2", 2, 3, 10, "clock", [], []),
        ]

        room = EscapeRoom(puzzles)

        result = room._choose_by_difficulty()

        mock_print.assert_any_call(
            "No puzzles with that level of difficulty. Try another."
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].difficulty, 1)

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
            RiddlePuzzle("R1", "Riddle 1", 2, 3, 10, "piano", [], []),
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

    @patch("builtins.input")
    @patch("builtins.print")
    def test_register_player_reprompts(self, mock_print, mock_input):
        mock_input.side_effect = ["", "Ana", "abc", "-5", "150", "21"]

        player = self.room.register_player()

        self.assertEqual(player.name, "Ana")
        self.assertEqual(player.age, 21)

        mock_print.assert_any_call("Name must be a non-empty string.")
        mock_print.assert_any_call("Age must be a valid non-negative integer.")

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
                "name": "Ana",
                "score": 10,
            },
        )

    def test_save_results_no_player(self):
        with self.assertRaises(ValueError):
            self.room.save_results("results.json")

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
    def test_play_puzzle_guess_word_shows_incorrect_guesses(
        self,
        mock_input,
        mock_print,
    ):
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
    def test_play_puzzle_reprompts_empty(
        self,
        mock_input,
        mock_print,
    ):
        self.room.player = Player("Ana", 20)
        puzzle = EquationPuzzle("E1", "Equation", 1, 3, 10, "x=1", 1)
        mock_input.side_effect = ["", "1"]

        result = self.room.play_puzzle(puzzle)

        self.assertTrue(result)
        mock_print.assert_any_call("Please enter a number.")
        self.assertEqual(self.room.player.score, 10)

    @patch("builtins.input")
    def test_play_puzzle_logic_runs(self, mock_input):
        self.room.player = Player("Ana", 20)
        puzzle = LogicPuzzle("L1", "Logic", 1, 2, 10, 2, "True/False")
        mock_input.return_value = "2"

        result = self.room.play_puzzle(puzzle)

        self.assertTrue(result)

    @patch("builtins.input")
    def test_play_puzzle_player_is_none(self, mock_input):
        with self.assertRaises(ValueError):
            self.room.player = None
            puzzle = LogicPuzzle("L1", "Logic", 1, 2, 10, 2, "True/False")
            mock_input.return_value = "2"

            self.room.play_puzzle(puzzle)

    def test_start_game_exits_from_menu(self):
        with (
            patch.object(self.room, "show_main_menu", return_value="exit"),
            patch.object(self.room, "register_player") as mock_register,
            patch("builtins.print") as mock_print,
        ):
            self.room.start_game()

        mock_register.assert_not_called()
        mock_print.assert_any_call("Goodbye!")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_start_game_handles_empty_selection(self, mock_input, mock_print):
        self.room.player = Player("Ana", 20)
        mock_input.return_value = "n"

        with (
            patch.object(self.room, "show_main_menu", return_value="start"),
            patch.object(
                self.room,
                "register_player",
                return_value=self.room.player,
            ),
            patch.object(self.room, "choose_puzzle_mode", return_value=[]),
            patch.object(self.room, "play_puzzle") as mock_play,
        ):
            self.room.start_game()

        mock_play.assert_not_called()
        mock_print.assert_any_call("No puzzles to play.")
