"""
Defines the MathPuzzle class - puzzle where the required answer is a mathematical result.

It extends the base Puzzle class. 
Defines a correct result. 

Attributes
----------
__correct_result: str
    The correct result to the puzzle.
"""

from .puzzle import Puzzle

class MathPuzzle(Puzzle):
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_result, attempts_made=0, is_solved=False):
        """
        Initializes a math-based puzzle with a correct result.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, attempts_made, is_solved)
        self.__correct_result = correct_result

    # Getter for the correct result
    def get_correct_result(self):
        return self.__correct_result

    def check_solution(self, user_input):
        """Check if the player's numeric answer is correct.

        Parameters
        ----------
        user_input: str
            The user's answer to the puzzle (the result entered).

        Returns
        -------
        bool
            True if the user's result is correct, False otherwise.

        """
        try:
            return float(user_input) == self.__correct_result
        except ValueError:
            return False
