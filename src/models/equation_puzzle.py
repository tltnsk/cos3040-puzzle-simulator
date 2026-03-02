"""
Defines the EquationPuzzle class
"""

from .math_puzzle import Puzzle

class EquationPuzzle(Puzzle):
    """
    Puzzle where the player solves a mathematical equation
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_result, equation_expression):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_result)
        self.__equation_expression = equation_expression

    def check_solution(self, user_input):
        """
        Check if the player's numeric answer is correct
        """
        try:
            return float(user_input) == self.get_correct_result()
        except ValueError:
            return False    
