"""
Abstract base class for numeric puzzle types.

Extends Puzzle class with a stored numeric result 
that subclasses will validate.
"""
from abc import ABC, abstractmethod

from .puzzle import Puzzle


class MathPuzzle(Puzzle, ABC):
    """
    MathPuzzle class
    Abstract class for numeric puzzles.
    """

    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_result, attempts_made=0, is_solved=False):
        """
        Initialize a numeric puzzle with its correct result.

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
        correct_result : float
            The correct result to the puzzle.
        attempts_made : int, optional
            Number of attempts already used.
        is_solved : bool, optional
            Whether the puzzle has already been solved.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, attempts_made, is_solved)
        self._correct_result = correct_result

    @property
    def correct_result(self):
        """Return the correct result for the puzzle."""
        return self._correct_result

    @abstractmethod
    def check_solution(self, user_input):
        """
        Abstract method to check if the player's numeric answer is correct.

        Parameters
        ----------
        user_input: str
            The user's answer to the puzzle (the result entered).

        Raises
        ------
        NotImplementedError
            If the method is not implemented in a subclass.
        """
        raise NotImplementedError(
            "Subclasses of math puzzle should implement "
            "the check_solution method"
        )