"""
Riddle puzzle class.

Represents text-answer riddles, supports accepted answer variations, and
provides hints.
"""

from .text_puzzle import TextPuzzle


class RiddlePuzzle(TextPuzzle):
    """
    RiddlePuzzle class
    Puzzle where the player guesses a riddle word.
    """

    def __init__(
        self,
        puzzle_id,
        description,
        difficulty,
        max_attempts,
        points,
        correct_answer,
        hints,
        allowed_variations=None,
        attempts_made=0,
        is_solved=False,
    ):
        """
        Initialize a riddle puzzle.

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
            The correct answer to the riddle.
        hints : list
            Hint messages shown one by one to the player.
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
            allowed_variations=allowed_variations,
            attempts_made=attempts_made,
            is_solved=is_solved,
        )

        self._hints = hints
        self._hints_used_count = 0

    @property
    def hints(self):
        """Returns the list of hints for the riddle."""
        return self._hints

    @property
    def hints_used_count(self):
        """Return the number of hints used so far."""
        return self._hints_used_count

    def use_hint(self):
        """
        Provides the next hint and increments the count of hints used.
        If no hints are available, it returns None.

        Returns
        -------
        str or None
            The next hint, or None if no hints are available.
        """
        if self._hints_used_count < len(self._hints):
            hint = self._hints[self._hints_used_count]
            self._hints_used_count += 1
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
        if self.solved:
            return True

        if self.attempts_made >= self.max_attempts:
            raise ValueError(
                "Maximum attempts reached. You cannot make more guesses."
            )

        if not isinstance(user_input, str):
            raise ValueError("Input must be a string.")

        # Normalize the user input and correct answer
        normalized_input = user_input.strip().lower()
        if not normalized_input:
            raise ValueError("Input cannot be empty.")

        correct_answer = self.correct_answer.strip().lower()
        normalized_variations = [
            variation.strip().lower()
            for variation in self.allowed_variations
        ]
        is_correct = (
            normalized_input == correct_answer
            or normalized_input in normalized_variations
        )

        # increase number of attempts made
        self.attempts_made += 1

        if is_correct:
            self.solved = True
            return True

        return False
