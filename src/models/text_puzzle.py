"""
Defines the TextPuzzle class - puzzle where the required answer is text-based
"""

from .puzzle import Puzzle

class TextPuzzle(Puzzle):
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, allowed_variations=None, attempts_made=0, is_solved=False):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, attempts_made, is_solved)
        self.__correct_answer = correct_answer
        self.__allowed_variations = allowed_variations or []
    
    def get_correct_answer(self):
        return self.__correct_answer

    def check_solution(self, user_input):
        """
        Check if the user's answer matches the correct answer or any allowed variation.
        """
        normalized_input = user_input.strip().lower()
        if normalized_input == self.__correct_answer.strip().lower():
            return True
        return normalized_input in [variation.strip().lower() for variation in self.__allowed_variations]

    
