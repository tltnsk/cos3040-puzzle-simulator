"""
Logic puzzle class.

Represents logic questions with numeric answers and can show the
explanation after several unsuccessful attempts.
"""
from .math_puzzle import MathPuzzle

import re


class LogicPuzzle(MathPuzzle):
    """
    LogicPuzzle class
    Puzzle that validates a numeric logical answer.
    """

    def __init__(
        self,
        puzzle_id,
        description,
        difficulty,
        max_attempts,
        points,
        correct_result,
        explanation,
        attempts_made=0,
        is_solved=False,
    ):
        """
        Initialize a logic puzzle.

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
        correct_result : int
            The expected numeric answer.
        explanation : str
            The explanation for the solution of the puzzle.
        attempts_made : int, optional
            Number of attempts already used.
        is_solved : bool, optional
            Whether the puzzle has already been solved.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_result, attempts_made, is_solved)
        self._explanation = explanation

    @property
    def explanation(self):
        """Returns the explanation for the correct answer as a string."""
        return self._explanation

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
            True if the user's answer is correct, False otherwise.
        """
        if self.solved:
            return True

        if self.attempts_made >= self.max_attempts:
            raise ValueError(
                "Maximum attempts reached. You cannot make more guesses."
            )

        if not re.match("^-?\d$", user_input):
            raise ValueError("Please enter a number.")

        if not user_input.strip():
            raise ValueError("Input cannot be empty.")

        self.attempts_made += 1
        
        try:
            user_result = int(user_input)
        except ValueError:
            return False

        is_correct = user_result == self.correct_result

        if is_correct:
            self.solved = True
        return is_correct
