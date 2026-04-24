"""
This class represents the game controller.

It handles menu flow, player registration, puzzle selection,
gameplay, and scoring.
"""

from copy import deepcopy

from src.models.player import Player
from src.models.puzzles.equation_puzzle import EquationPuzzle
from src.models.puzzles.guess_word_puzzle import GuessWordPuzzle
from src.models.puzzles.logic_puzzle import LogicPuzzle
from src.models.puzzles.riddle_puzzle import RiddlePuzzle
from src.utils.result_manager import append_result

# Look up table for puzzle type labels.
_PUZZLE_TYPE_LABELS = {
    "guess_word": "Guess word",
    "riddle": "Riddle",
    "equation": "Equation",
    "logic": "Logic",
}


class EscapeRoom:
    """
    EscapeRoom class.
    Game controller.
    """

    def __init__(self, puzzles):
        """
        Initialize the EscapeRoom game with a list of puzzles.

        Args
        ----------
        puzzles : list
            A list of puzzle objects.
        """
        self.puzzles = puzzles
        self.player = None

    @property
    def puzzles(self):
        """Returns the puzzles in the escape room."""
        return self._puzzles

    @puzzles.setter
    def puzzles(self, puzzles):
        """Sets the puzzles for the escape room."""
        if puzzles is None:
            raise ValueError("Puzzles cannot be None.")
        self._puzzles = deepcopy(puzzles)

    @property
    def player(self):
        """Returns the current player."""
        return self._player

    @player.setter
    def player(self, player):
        """Sets the current player."""
        if player is not None and not isinstance(player, Player):
            raise ValueError("Not an instance of Player class.")
        self._player = player

    def start_game(self, results_file_path=None):
        """
        Start the game.

        1) Show a menu (start / exit)
        2) Register player
        3) Let player choose puzzles (type/difficulty)
        4) Play puzzles and update score
        5) Save results to a file (if file path is given)

        Args:
            results_file_path (str, optional): Path to write results.
                If the file name is not given, results are not saved.
        """
        while True:
            choice = self.show_main_menu()
            if choice == "exit":
                print("Goodbye!")
                return
            if choice == "instructions":
                self._show_instructions()
                continue
            if choice == "start":
                break

        self.register_player()

        while True:
            to_play = self.choose_puzzle_mode()
            if to_play:
                for puzzle in to_play:
                    self.play_puzzle(puzzle)
            else:
                print("No puzzles to play.")

            again = input("\nPlay another game? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                break

        if results_file_path is not None:
            self.save_results(results_file_path)
            print(f"\nResults saved to {results_file_path}")

    def _show_instructions(self):
        """Print short gameplay instructions."""
        print(
            "\n--- Instructions ---\n"
            "Answer text puzzles with a word or phrase.\n"
            "For riddles, type 'hint' to see the next hint (if available).\n"
            "For math puzzles, enter a number.\n"
        )

    def register_player(self):
        """
        Ask the user for player details (name, age) and create a Player.

        Returns
        -------
        Player
            The newly created player.
        """
        print("\n--- Player registration ---")
        while True:
            name = input("Enter your name: ").strip()
            try:
                player = Player(name, 20)
                break
            except ValueError as error:
                print(str(error))

        while True:
            str_age = input("Enter your age: ").strip()
            try:
                age = int(str_age)
                player.age = age
                break
            except ValueError as error:
                    print("Age must be a valid non-negative integer.")
            except TypeError:
                print("Age must be a whole number.")
                continue

        self.player = player
        print(f"\nWelcome, {player.name}!")
        return player

    def show_main_menu(self):
        """
        Display the main menu (start, instructions, exit).

        Returns
        -------
        str
            `"start"`, `"instructions"`, or `"exit"`.
        """
        print("\n=== Escape Room — Main Menu ===")
        print("1) Start game")
        print("2) Instructions")
        print("3) Exit")

        while True:
            choice = input("Choose an option (1-3): ").strip()
            if choice == "1":
                return "start"
            if choice == "2":
                return "instructions"
            if choice == "3":
                return "exit"
            print("Please enter 1, 2, or 3.")

    def choose_puzzle_mode(self):
        """
        Let the player choose puzzles by type or difficulty.

        Returns:
            list: A list of puzzle instances to play (may be empty).
        """
        print("\n--- Choose puzzles ---")
        print("1) By puzzle type")
        print("2) By difficulty (1 easy, 2 medium, 3 hard) ")

        while True:
            mode = input("Choose 1 or 2: ").strip()
            if mode == "1":
                return self._choose_by_type()
            if mode == "2":
                return self._choose_by_difficulty()

            print("Please enter 1 or 2.")

    def _choose_by_type(self):
        """Ask the user for a puzzle type and return filtered puzzles."""
        print("\nPuzzle types:")
        for key, label in _PUZZLE_TYPE_LABELS.items():
            print(f"  - {key} ({label})")

        while True:
            puzzle_type = input(
                "Enter puzzle type (e.g. guess_word): "
            ).strip().lower()
            if puzzle_type in _PUZZLE_TYPE_LABELS:
                filtered = self.filter_puzzles_by_type(puzzle_type)
                if not filtered:
                    print("Such type of puzzle does not exist. Try another.")
                    continue
                return deepcopy(filtered)
            print(
                "Unknown type. Choose one of: "
                f"{', '.join(_PUZZLE_TYPE_LABELS)}"
            )

    def _choose_by_difficulty(self):
        """
        Ask the user to enter the level of difficulty 1-3.

        Return filtered puzzles.
        """
        while True:
            puzzle_difficulty = input(
                "Enter difficulty (1, 2, or 3): "
            ).strip()
            if puzzle_difficulty in ("1", "2", "3"):
                difficulty = int(puzzle_difficulty)
                filtered = self.filter_puzzles_by_difficulty(difficulty)
                if not filtered:
                    print(
                        "No puzzles with that level of difficulty. "
                        "Try another."
                    )
                    continue
                return deepcopy(filtered)
            print("Please enter 1, 2, or 3.")

    def filter_puzzles_by_type(self, puzzle_type):
        """
        Return puzzles filtered by type.

        Parameters
        ----------
        puzzle_type : str
            Puzzle type entered by the player.

        Returns:
            list: Puzzles whose class matches the given type.

        Raises:
            ValueError: If puzzle_type is not recognized.
        """
        key = puzzle_type.strip().lower()
        type_map = {
            "guess_word": GuessWordPuzzle,
            "riddle": RiddlePuzzle,
            "equation": EquationPuzzle,
            "logic": LogicPuzzle,
        }
        puzzle = type_map.get(key)
        if puzzle is None:
            raise ValueError(
                f"Unknown puzzle type '{puzzle_type}'. "
                f"Expected one of: {', '.join(type_map)}"
            )
        return [p for p in self.puzzles if isinstance(p, puzzle)]

    def filter_puzzles_by_difficulty(self, difficulty):
        """
        Return puzzles filtered by difficulty.

        Args:
            difficulty (int): Difficulty level (1, 2, or 3).

        Returns:
            list: Puzzles at that difficulty.
        """
        return [p for p in self.puzzles if p.difficulty == difficulty]

    def play_puzzle(self, puzzle):
        """Run the interaction loop for a single puzzle."""
        if self.player is None:
            raise ValueError("No player is set.")

        # Make sure puzzles are playable even if reused.
        try:
            puzzle.solved = False
            puzzle.attempts_made = 0
        except Exception:
            pass

        puzzle_type = "Puzzle"
        if isinstance(puzzle, GuessWordPuzzle):
            puzzle_type = "Guess word"
        elif isinstance(puzzle, RiddlePuzzle):
            puzzle_type = "Riddle"
        elif isinstance(puzzle, EquationPuzzle):
            puzzle_type = "Equation"
        elif isinstance(puzzle, LogicPuzzle):
            puzzle_type = "Logic"

        print(f"\n--- {puzzle_type} ({puzzle.id}) ---")
        print(
            f"Difficulty: {puzzle.difficulty} | "
            f"Points: {puzzle.points} | "
            f"Attempts: {puzzle.max_attempts}"
        )
        print(puzzle.description)

        if isinstance(puzzle, RiddlePuzzle):
            print("Type 'hint' to get a hint (doesn't use an attempt).")

        while not puzzle.solved and puzzle.attempts_made < puzzle.max_attempts:
            if isinstance(puzzle, (EquationPuzzle, LogicPuzzle)):
                prompt = "Your answer (number): "
            else:
                prompt = "Your answer: "

            user_input = input(prompt).strip()

            if (
                isinstance(puzzle, RiddlePuzzle)
                and user_input.lower() == "hint"
            ):
                hint = puzzle.use_hint()
                if hint is None:
                    print("No more hints.")
                else:
                    print(f"Hint: {hint}")
                continue

            try:
                is_correct = puzzle.check_solution(user_input)
            except ValueError as exc:
                print(str(exc))
                continue

            if is_correct:
                print("Correct!")
                self.update_score(puzzle.points)
                print(f"Score: {self.player.score}")
                return True

            remaining = puzzle.max_attempts - puzzle.attempts_made
            print(f"Incorrect. Attempts remaining: {remaining}")
            if (
                isinstance(puzzle, GuessWordPuzzle)
                and puzzle.incorrect_guesses
            ):
                last_few = puzzle.incorrect_guesses[-3:]
                print(f"Incorrect guesses: {', '.join(last_few)}")

        print("Puzzle not solved.")
        if isinstance(puzzle, LogicPuzzle):
            print(f"Explanation: {puzzle.explanation}")
        return False

    def update_score(self, points):
        """Update the player's score when they solve a puzzle."""
        if self.player is None:
            raise ValueError("No player is set.")
        self.player.add_score(points)

    def save_results(self, file_path):
        """
        Save the player's results to a file.

        Parameters
        ----------
        file_path : str
            Path to the results JSON file.
        """
        if self.player is None:
            raise ValueError("No player is set.")

        append_result(
            file_path,
            {
                "name": self.player.name,
                "score": self.player.score,
            }
        )
