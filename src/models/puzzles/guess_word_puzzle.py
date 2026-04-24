"""
Guess-word puzzle class.

Represents text puzzles where the player guesses a hidden word.
The puzzle tracks the incorrect guesses made.
"""

import re

from .text_puzzle import TextPuzzle


class GuessWordPuzzle(TextPuzzle):
    """
    GuessWordPuzzle class
    Puzzle where the player has to guess a word with several letters provided.
    """

    def __init__(
        self,
        puzzle_id,
        description,
        difficulty,
        max_attempts,
        points,
        correct_answer,
        allowed_variations=None,
        attempts_made=0,
        is_solved=False,
    ):
        """
        Initialize a guess-word puzzle.

        Parameters
        ----------
        puzzle_id : str
            Unique ID for the puzzle.
        description : str
            Puzzle description shown to the player.
        difficulty : int
            Puzzle difficulty level.
        max_attempts : int
            Maximum number of guesses allowed.
        points : int
            Points awarded for solving the puzzle.
        correct_answer : str
            The correct hidden word.
        allowed_variations : list, optional
            Other accepted answers for the puzzle.
        attempts_made : int, optional
            Number of attempts already used.
        is_solved : bool, optional
            Whether the puzzle has already been solved.
        """
        super().__init__(
            puzzle_id,
            description,
            difficulty,
            max_attempts,
            points,
            correct_answer,
            allowed_variations,
            attempts_made,
            is_solved,
        )
        self._incorrect_guesses = []

    @property
    def incorrect_guesses(self):
        """Returns a list of incorrect guesses made by the player."""
        return self._incorrect_guesses

    def add_incorrect_guess(self, guess):
        """
        Add an incorrect guess to the list of incorrect guesses.

        Parameters
        ----------
        guess : str
            The player's incorrect guess.
        """
        self._incorrect_guesses.append(guess)

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
            raise ValueError(
                "Maximum attempts reached. You cannot make more guesses."
            )

        if not isinstance(user_input, str):
            raise ValueError("Input must be a string.")

        normalized_input = user_input.strip().lower()
        if not normalized_input:
            raise ValueError("Input cannot be empty.")

        # Allow only letters and spaces in the guess word
        if not re.fullmatch(r"[A-Za-z]+( [A-Za-z]+)*", normalized_input):
            raise ValueError("Input must contain only letters and spaces.")

        correct_answer = self.correct_answer.strip().lower()

        normalized_variations = [
            variation.strip().lower()
            for variation in self.allowed_variations
        ]
        
        is_correct = (
            normalized_input == correct_answer
            or normalized_input in normalized_variations
        )

        self.attempts_made += 1

        if is_correct:
            self.solved = True
            return True

        self.add_incorrect_guess(user_input)
        return False
