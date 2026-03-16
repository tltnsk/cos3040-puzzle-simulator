"""
Defines the EquationPuzzle class.

This class represents a puzzle where the player solves a mathematical equation. 
The player's answer is validated against the correct result.
Tolerance for floating-point comparisons is also included.
"""
import math
from .math_puzzle import MathPuzzle

class EquationPuzzle(MathPuzzle):
    """
    EquationPuzzle class
    Puzzle where the player solves a mathematical equation
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, equation, correct_result, tolerance=1e-9, attempts_made=0, is_solved=False):
        """
        Initializes an equation-based puzzle.

        Args 
        ----------
        __equation: str
            The mathematical equation to be solved. (e.g. 2x = 5)
        __tolarance: float
            The tolerance for floating-point comparisson. 
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_result, attempts_made, is_solved)
        self.__equation = equation
        self.__tolerance = tolerance  

    @property 
    def equation(self):
        """Return the equation to be solved as a string."""
        return self.__equation

    @property 
    def tolerance(self):
        """Returns the toleerance for floating-point comparisson"""
        return self.__tolerance 

    def check_solution(self, user_input):
        """
        Check if the player's numeric answer is correct within a tolerance.

        Parameters
        ----------
        user_input : str
            The user's answer to the puzzle.

        Returns
        -------
        bool
            True if the user's result is correct within the tolerance, False otherwise.
        """
        try:
            user_result = float(user_input)
            # Compare user result to the correct result with allowed tolerance
            self.set_attempts_made(self.get_attempts_made() + 1)
            is_correct = math.isclose(user_result, self.get_correct_result(), rel_tol=self.__tolerance)
            if is_correct:
                self.set_solved(True)
            return is_correct
        except ValueError:
            return False
