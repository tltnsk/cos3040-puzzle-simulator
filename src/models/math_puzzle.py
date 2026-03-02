"""
Defines the MathPuzzle class - puzzle where the required answer is a mathematical result
"""

from .puzzle import Puzzle

class MathPuzzle(Puzzle):
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_result):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points)
        self.__correct_result = correct_result
