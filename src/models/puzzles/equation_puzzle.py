"""
Equation puzzle class.

Represents puzzles that expect a numeric solution to an equation.
It validates player input using floating-point tolerance.
"""
import math
import re

from .math_puzzle import MathPuzzle


class EquationPuzzle(MathPuzzle):
    """
    EquationPuzzle class
    Puzzle where the player solves a mathematical equation
    """

    def __init__(
        self,
        puzzle_id,
        description,
        difficulty,
        max_attempts,
        points,
        equation,
        correct_result,
        tolerance=1e-9,
        attempts_made=0,
        is_solved=False,
    ):
        """
        Initialize an equation-based puzzle.

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
        equation : str
            The mathematical equation to be solved. (e.g. 2x = 5)
        correct_result : float
            The numeric result expected from the player.
        tolerance : float, optional
            The tolerance for floating-point comparison.
        attempts_made : int, optional
            Number of attempts already used.
        is_solved : bool, optional
            Whether the puzzle has already been solved.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_result, attempts_made, is_solved)
        self._equation = equation
        self._tolerance = tolerance

    @property
    def equation(self):
        """Return the equation to be solved as a string."""
        return self._equation

    @property
    def tolerance(self):
        """Return the tolerance used for floating-point comparison."""
        return self._tolerance

    def check_solution(self, user_input):
        """
        Check if the player's numeric answer is correct.

        Parameters
        ----------
        user_input : str
            The user's answer to the puzzle.

        Returns
        -------
        bool
            True if the user's result is correct within the tolerance,
            False otherwise.
        """
        if self.solved:
            return True

        if self.attempts_made >= self.max_attempts:
            raise ValueError(
                "Maximum attempts reached. You cannot make more guesses."
            )

        if not re.match("^-?\d+\.?\d*$", user_input):
            raise ValueError("Please enter a number.")

        if not user_input.strip():
            raise ValueError("Input cannot be empty.")

        # Count attempt (regardless of correctness).
        self.attempts_made += 1

        try:
            user_result = float(user_input)
        except ValueError:
            return False
        
        # Check if an answer is correct within a tolerance
        is_correct = math.isclose(
            user_result,
            self.correct_result,
            rel_tol=self._tolerance,
        )

        if is_correct:
            self.solved = True
        return is_correct