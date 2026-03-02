"""
Defines the MathPuzzle class - puzzle where the required answer is a mathematical result
"""

from .puzzle import Puzzle

class MathPuzzle(Puzzle):
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_result, attempts_made=0, is_solved=False):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, attempts_made, is_solved)
        self.__correct_result = correct_result

    def get_correct_result(self):
        return self.__correct_result

    def check_solution(self, user_input):
        """
        Check if the player's numeric answer is correct.
        """
        try:
            return float(user_input) == self.__correct_result
        except ValueError:
            return False
