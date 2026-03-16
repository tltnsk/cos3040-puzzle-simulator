"""
Defines the MathPuzzle class - puzzle where the required answer is a mathematical result.

It extends the base Puzzle class. 
Defines a correct result. 

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
        Initializes a math-based puzzle with a correct result.
        Args
        ----------
        __correct_result: float
            The correct result to the puzzle.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, attempts_made, is_solved)
        self.__correct_result = correct_result

    @property
    def correct_result(self):
        """Return the correct result for the puzzle"""
        return self.__correct_result

    @abstractmethod
    def check_solution(self, user_input):
        """
        Abstract method to check if the player's numeric answer is correct.

        Parameters
        ----------
        user_input: str
            The user's answer to the puzzle (the result entered).

        Returns
        -------
        bool
            True if the user's result is correct, False otherwise.

        """
        raise NotImplementedError("Subclasses of math puzzle should implement the check_solution method")