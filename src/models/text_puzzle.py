"""
Defines the TextPuzzle class - puzzle where the required answer is text-based

It extends the base Puzzle class. 
Defines a correct answer and also allowed variations.

Attributes
----------
__correct_answer: str
    The correct answer to the puzzle.

__allowed_variations: list
    List of acceptable variations for the correct answer.
"""

from .puzzle import Puzzle

class TextPuzzle(Puzzle):
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, allowed_variations=None, attempts_made=0, is_solved=False):
        
        """
        Initializes a text-based puzzle with a correct answer and allowed variations.
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, attempts_made, is_solved)
        self.__correct_answer = correct_answer
        self.__allowed_variations = allowed_variations or []

    # Getter for the correct answer
    def get_correct_answer(self):
        return self.__correct_answer

    def check_solution(self, user_input):
        """Check if the user's answer matches the correct answer or any allowed variation.

        Parameters
        ----------
        user_input: str
            The user's answer to the puzzle.

        Returns
        -------
        bool
            True if the user's answer is correct, False otherwise.

        """

        # Increase the attempts made
        # Also handles logic to check whether attempts made exceeds max attempt
        self.set_attempts_made(self.get_attempts_made() + 1)

        # Validate user input - it shouldn't be empty and it should be a string 
        if not user_input or not isinstance(user_input, str):
            return False
        
        # Normalize input and compare it to the correct answer
        normalized_input = user_input.strip().lower()
        if normalized_input == self.__correct_answer.strip().lower():
            return 
        
        # Check if the input matches any of the allowed variations
        return normalized_input in [variation.strip().lower() for variation in self.__allowed_variations]

    
