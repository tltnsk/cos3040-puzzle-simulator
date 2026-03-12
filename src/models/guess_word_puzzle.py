"""
Defines the GuessWordPuzzle class.

This class is a puzzle which requires the player to guess a word which has some missing letters.
The answer needs to be a string.
The player's answer is validated against the correct result.
"""

from .text_puzzle import TextPuzzle

class GuessWordPuzzle(TextPuzzle):  
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, allowed_variations=None, attempts_made=0):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_answer, allowed_variations)
        self.__incorrect_guesses = [] # initialize an empty list for incorrect guesses
    
    def check_solution(self, user_input):
        """
        Check if the guessed word matches the correct answer.

        Parameters
        ----------
        user_input : str
            The player's guess.

        Returns
        -------
        bool
            True if the guess is correct, False otherwise.
        """
        if user_input.strip().lower() == self.get_correct_answer().lower():
            return True
        else:
            self.add_incorrect_guess(user_input)  # Track incorrect guess
            self.set_attempts_made(self.get_attempts_made() + 1)  # Increment attempts
            return False
    
    def add_incorrect_guess(self, guess):
        """
        Add an incorrect guess to the list of incorrect guesses.

        Parameters
        ----------
        guess : str
            The player's incorrect guess.
        """
        self.__incorrect_guesses.append(guess)

    def get_incorrect_guesses(self):
        """
        Get the list of incorrect guesses.

        Returns
        -------
        list
            A list of incorrect guesses made by the player.
        """
        return self.__incorrect_guesses