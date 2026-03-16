"""
Defines the LogicPuzzle class.

This class represents a puzzle where the player solves a logic problem.
The provided answer needs to be an integer.  
The player's answer is validated against the correct result.
"""
from .math_puzzle import MathPuzzle

class LogicPuzzle(MathPuzzle):
    """
    LogicPuzzle class 
    Puzzle that validates a numeric logical answer.
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_result, explanation, attempts_made=0, is_solved=False):
        """
        Initializes an equation-based puzzle.

        Args 
        ----------
        __explanation: str
            The explanation for the solution of the puzzle.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_result, attempts_made, is_solved)
        self.__explanation = explanation

    @property
    def explanation(self):
        """Returns the explanation for the correct answer as a string."""
        return self.__explanation

    def check_solution(self, user_input):
        """
        Check if the player's numeric answer is correct

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
            raise ValueError("Maximum attempts reached. You cannot make more guesses.")

        if not isinstance(user_input, str):
            raise ValueError("Input must be a string.")

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
