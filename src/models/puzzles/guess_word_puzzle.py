"""
Defines the GuessWordPuzzle class.

This class is a puzzle which requires the player to guess a word which has some missing letters.
The answer needs to be a string.
The player's answer is validated against the correct answer.
"""

from .text_puzzle import TextPuzzle

class GuessWordPuzzle(TextPuzzle):  
    """
    GuessWordPuzzle class
    Puzzle where the player has to guess a word with several letters provided.
    """
    def __init__(self, puzzle_id, description, difficulty, max_attempts,
                 points, correct_answer, allowed_variations=None, attempts_made=0, is_solved=False):
        """
        Initializes a guess-word puzzle.

        Args 
        ----------
        __incorrect_guesses: list
            A list storing the player's incorrect guesses
        """
        super().__init__(puzzle_id, description, difficulty, max_attempts,
                         points, correct_answer, allowed_variations, attempts_made, is_solved)
        self.__incorrect_guesses = []

    @property
    def incorrect_guesses(self):
        """Returns a list of incorrect guesses made by the player."""
        return self.__incorrect_guesses
    
    def add_incorrect_guess(self, guess):
        """
        Add an incorrect guess to the list of incorrect guesses.

        Parameters
        ----------
        guess : str
            The player's incorrect guess.
        """
        self.__incorrect_guesses.append(guess)
    
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
        if self.solved:
            return True
        
        if self.attempts_made >= self.max_attempts:
            raise ValueError("Maximum attempts reached. You cannot make more guesses.")
        
        if not isinstance(user_input, str):
            raise ValueError("Input must be a string.")
    
        normalized_input = user_input.strip().lower()
        if not normalized_input:
            raise ValueError("Input cannot be empty.")

        correct_answer = self.correct_answer.strip().lower()
        normalized_variations = [v.strip().lower() for v in self.allowed_variations]
        is_correct = normalized_input == correct_answer or normalized_input in normalized_variations

        self.attempts_made += 1

        if is_correct:
            self.solved = True
            return True

        self.add_incorrect_guess(user_input)
        return False
   
