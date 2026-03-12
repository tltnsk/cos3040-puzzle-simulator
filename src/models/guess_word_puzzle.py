"""
Defines the GuessWordPuzzle class.

This class is a puzzle which requires the player to guess a word which has some missing letters.
The answer needs to be a string.
The player's answer is validated against the correct answer.
"""

from .text_puzzle import TextPuzzle

class GuessWordPuzzle(TextPuzzle):  
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, allowed_variations=None, attempts_made=0, is_solved=False):
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_answer, allowed_variations, attempts_made, is_solved)
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
        is_correct = super().check_solution(user_input)
        if not is_correct and isinstance(user_input, str) and user_input.strip():
            self.add_incorrect_guess(user_input)
        return is_correct
    
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