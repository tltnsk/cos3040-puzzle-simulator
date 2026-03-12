"""
Defines the RiddlePuzzle class

This class is a puzzle which requires the player to guess the solution of a riddle.
The answer needs to be a string.
The player's answer is validated against the correct answer.
"""

from .text_puzzle import TextPuzzle

class RiddlePuzzle(TextPuzzle):
    """
    Puzzle where the player guesses a riddle word
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, hints, attempts_made=0, is_solved=False):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_answer, allowed_variations=None, attempts_made=attempts_made, is_solved=is_solved)
        
        self.__hints = hints
        self.__hints_used_count = 0

    def get_hints(self):
        """
        Get the list of hints for the puzzle.

        Returns
        -------
        list
            The list of hints for the riddle.
        """
        return self.__hints
    
    def get_hints_used_count(self):
        """
        Get the number of hints used so far.

        Returns
        -------
        int
            The number of hints used.
        """
        return self.__hints_used_count
    
    def use_hint(self):
        """
        Returns the next hint if available.

        Provides the next hint and increments the count of hints used. 
        If no hints are available, it returns None.

        Returns
        -------
        str or None
            The next hint, or None if no hints are available.
        """
        if self.__hints_used_count < len(self.__hints):
            hint = self.__hints[self.__hints_used_count]
            self.__hints_used_count += 1
            return hint
        return None

    def check_solution(self, user_input):
        """
        Check if the player's answer matches the correct riddle answer.

        Parameters
        ----------
        user_input : str
            The player's answer.

        Returns
        -------
        bool
            True if the answer is correct, False otherwise.
        """
        return super().check_solution(user_input)
