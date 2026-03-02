"""
Defines the RiddlePuzzle class 
"""

from .text_puzzle import TextPuzzle

class RiddlePuzzle(TextPuzzle):
    """
    Puzzle where the player guesses a riddle word
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, hints):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_answer)
        
        self.__hints = hints
        self.__hints_used_count = 0

    def get_hints(self):
        return self.__hints
    
    def get_hints_used_count(self):
        return self.__hints_used_count
    
    def use_hint(self):
        """
        Returns the next hint if available
        """
        if self.__hints_used_count < len(self.__hints):
            hint = self.__hints[self.__hints_used_count]
            self.__hints_used_count += 1
            return hint
        return None

    def check_solution(self, user_input):
        """
        Check if the player's answer matches the correct riddle answer
        """
        return user_input.strip().lower() == self.get_correct_answer().strip().lower()