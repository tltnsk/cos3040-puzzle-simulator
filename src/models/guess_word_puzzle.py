"""
Defines the GuessWordPuzzle class
"""

from .text_puzzle import TextPuzzle

class GuessWordPuzzle(TextPuzzle):
    """Puzzle where the player guesses a word"""    
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, allowed_variations=None, attempts_made=0):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_answer, allowed_variations)
        self.__attempts_made = attempts_made
    
    def check_solution(self, user_input):
        """Check if the guessed word matches the correct answer"""
        return user_input.strip().lower() == self.get_correct_answer().lower()