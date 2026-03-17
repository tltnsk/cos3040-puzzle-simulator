"""
Defines the EscapeRoom class.

Runs the game and controls puzzle display and scoring.

"""

from copy import deepcopy
from models.player import Player

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
        return self.__puzzles

    @puzzles.setter
    def puzzles(self, puzzles):
        """Sets the puzzles for the escape room."""
        if puzzles is None:
            raise ValueError("Puzzles cannot be None.")
        self.__puzzles = deepcopy(puzzles)

    @property
    def player(self):
        """Returns the current player."""
        return self.__player

    @player.setter
    def player(self, player):
        """Sets the current player."""
        if player is not None and not isinstance(player, Player):
            raise ValueError("Not an instance of Player class.")
        self.__player = player

    # Method headings

    def start_game(self):
        """
        Start the game.

        1) Show a menu (start / exit)
        2) Register player
        3) Let player choose puzzles (type/difficulty)
        4) Play puzzles and update score
        5) Save results to a file
        """
        raise NotImplementedError

    def register_player(self):
        """Ask the user for player details (name, age) and create a Player."""
        raise NotImplementedError

    def show_main_menu(self):
        """Display the main menu (start, instructions, exit)."""
        raise NotImplementedError

    def choose_puzzle_mode(self):
        """Let the player choose puzzles by type or difficulty."""
        raise NotImplementedError

    def filter_puzzles_by_type(self, puzzle_type):
        """Return puzzles filtered by type."""
        raise NotImplementedError

    def filter_puzzles_by_difficulty(self, difficulty):
        """Return puzzles filtered by difficulty."""
        raise NotImplementedError

    def play_puzzle(self, puzzle):
        """Run the interaction loop for a single puzzle."""
        raise NotImplementedError

    def update_score(self, points):
        """Update the player's score when they solve a puzzle."""
        if self.player is None:
            raise ValueError("No player is set.")
        self.player.add_score(points)

    def save_results(self, file_path):
        """Save the player's results (id, name, score) to a file."""
        raise NotImplementedError
