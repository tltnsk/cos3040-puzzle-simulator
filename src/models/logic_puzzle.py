"""
Defines the LogicPuzzle class
"""
from .math_puzzle import MathPuzzle

class LogicPuzzle(MathPuzzle):
    """
    Puzzle that validates a numeric logical answer.
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_result, explanation):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_result)
        self.__explanation = explanation

    def check_solution(self, user_input):
        """
        Check if the player's numeric answer is correct
        """
        try:
            return float(user_input) == self.get_correct_result()
        except ValueError:
            return False