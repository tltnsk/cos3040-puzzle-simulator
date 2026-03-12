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
    Puzzle where the player solves a mathematical equation
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, equation, correct_result, tolerance=1e-9, attempts_made=0, is_solved=False):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_result, attempts_made, is_solved)
        """
        Intitalizes an equaiton-based puzzle.

        Parameters
        ----------
        equation: str
            The mathematical equation to be solved. (e.g. 2x = 5)
        correct_result: float
            The precomputed correct result of the equation.
        """
        self.__equation = equation
        self.__tolerance = tolerance  # Tolerance for floating-point comparison


    def get_equation(self):
        """
        Getter for the equation to be solved.
        Returns
        -------
        str
            The equation as a string 
        """
        return self.__equation

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
            return math.isclose(user_result, self.get_correct_result(), rel_tol=self.__tolerance)
        except ValueError:
            return False
