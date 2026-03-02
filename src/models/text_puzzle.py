"""
Defines the TextPuzzle class - puzzle where the required answer is text-based
"""

from .puzzle import Puzzle

class TextPuzzle(Puzzle):
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, allowed_variations=None):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points)
        self.__correct_answer = correct_answer
        self.__allowed_variations = allowed_variations or []
    
    def get_correct_answer(self):
        return self.__correct_answer

    