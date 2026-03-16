"""
Defines the TextPuzzle class - puzzle where the required answer is text-based

It extends the base Puzzle class. 
Defines a correct answer and also allowed variations.

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
        Initializes a text-based puzzle.
        Args
        ----------
        __correct_answer: str
            The correct answer to the puzzle.

        __allowed_variations: list
            List of acceptable variations for the correct answer.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, attempts_made, is_solved)
        self.__correct_answer = correct_answer
        self.__allowed_variations = allowed_variations or []

    @property
    def correct_answer(self):
        """Return the correct answer for the puzzle."""
        return self.__correct_answer
    
    @property 
    def allowed_variations(self):
        """Returns a list of acceptable variations for the correct answer."""
        return self.__allowed_variations

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
