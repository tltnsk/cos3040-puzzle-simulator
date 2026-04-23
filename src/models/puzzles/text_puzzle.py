"""
Abstract base class for text-based puzzle types.

Extends Puzzle with a correct text answer and optional accepted variations
that concrete text puzzles can compare user input against.
"""
from abc import ABC, abstractmethod
from .puzzle import Puzzle

class TextPuzzle(Puzzle, ABC):
    """
    TextPuzzle class
    Abstract class for text-based puzzles.
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, allowed_variations=None, attempts_made=0, is_solved=False):
        """
        Initialize a text-based puzzle.

        Parameters
        ----------
        puzzle_id : str
            Unique ID for the puzzle.
        description : str
            Puzzle description shown to the player.
        difficulty : int
            Puzzle difficulty level.
        max_attempts : int
            Maximum number of guesses allowed.
        points : int
            Points awarded for solving the puzzle.
        correct_answer : str
            The correct answer to the puzzle.
        allowed_variations : list, optional
            List of acceptable variations for the correct answer.
        attempts_made : int, optional
            Number of attempts already used.
        is_solved : bool, optional
            Whether the puzzle has already been solved.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, attempts_made, is_solved)
        self._correct_answer = correct_answer
        self._allowed_variations = allowed_variations or []

    @property
    def correct_answer(self):
        """Return the correct answer for the puzzle."""
        return self._correct_answer
    
    @property 
    def allowed_variations(self):
        """Returns a list of acceptable variations for the correct answer."""
        return self._allowed_variations

    @abstractmethod
    def check_solution(self, user_input):
        """
        Abstract method to check if the user's answer matches the correct answer or any allowed variation.

        Parameters
        ----------
        user_input: str
            The user's answer to the puzzle.

        Returns
        -------
        bool
            True if the user's answer is correct, False otherwise.
        """
        raise NotImplementedError("Subclasses which are text puzzles must implement the 'check_solution' method.")
