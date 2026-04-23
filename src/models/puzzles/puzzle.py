"""
Abstract base class for all puzzle types.

Provides shared puzzle state, common attributes, and the
method that concrete puzzle classes implement to check solutions.
"""

# Make Puzzle class abstract. Subclasses must implement the abstract method 
from abc import ABC, abstractmethod

class Puzzle(ABC):
    """Puzzle class"""
    def __init__(self, puzzle_id, description, difficulty, max_attempts, points, attempts_made=0, is_solved=False):
        """
        Initialize a puzzle with its shared attributes.

        Parameters
        ----------
        puzzle_id : str
            Unique ID for the puzzle.
        description : str
            Description of the puzzle.
        difficulty : int
            Level of difficulty (1 - easy, 2 - medium, 3 - hard)
        max_attempts : int
            Maximum number of attempts allowed.
        points : int
            Points for solving the puzzle 
        attempts_made : int, optional
            Number of attempts made so far.
        is_solved : bool, optional
            Whether the puzzle has been solved or not
        """     
        self._id = puzzle_id
        self.description = description
        self.difficulty = difficulty
        self.max_attempts = max_attempts
        self.attempts_made = attempts_made
        self.points = points
        self._is_solved = is_solved

    @property
    def id(self):
        """Returns the unique ID of the puzzle."""
        return self._id

    @property
    def description(self):
        """Returns the description of the puzzle."""
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of the puzzle."""
        self._description = description

    @property
    def difficulty(self):
        """Returns the difficulty level of the puzzle."""
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        """Sets the difficulty level of the puzzle."""
        if difficulty not in [1, 2, 3]:  # 1 - easy, 2 - medium, 3 - hard
            raise ValueError("Invalid difficulty level. Difficulty must be 1, 2, or 3.")
        self._difficulty = difficulty

    @property
    def max_attempts(self):
        """Returns the maximum number of attempts allowed for the puzzle."""
        return self._max_attempts

    @max_attempts.setter
    def max_attempts(self, max_attempts):
        """Sets the maximum number of attempts allowed for the puzzle."""
        if max_attempts < 0:
            raise ValueError("Maximum attempts cannot be negative.")
        self._max_attempts = max_attempts

    @property
    def attempts_made(self):
        """Returns the number of attempts made so far."""
        return self._attempts_made

    @attempts_made.setter
    def attempts_made(self, attempts_made):
        """Sets the number of attempts made so far."""
        if attempts_made < 0:
            raise ValueError("Attempts made cannot be negative")
        elif attempts_made > self._max_attempts:
            raise ValueError("Attempts made cannot exceed maximum attempts.")
        self._attempts_made = attempts_made

    @property
    def points(self):
        """Returns the points for solving the puzzle."""
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points for solving the puzzle."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self._points = points

    @property
    def solved(self):
        """Returns whether the puzzle has been solved."""
        return self._is_solved

    @solved.setter
    def solved(self, is_solved):
        """Sets whether the puzzle has been solved."""
        self._is_solved = is_solved

    def __str__(self):
        """Return a readable summary of the puzzle."""
        return f"Puzzle {self.id}: {self.description} (Difficulty {self.difficulty})"

    def __lt__(self, other):
        """
        Check if one the current EquationPuzzle is less difficult than other EquationPuzzle.

        Parameters
        ----------
        other : EquationPuzzle
            Another EquationPuzzle instance to compare with.

        Returns
        -------
        bool
            True if the puzzle is less difficult than the other puzzle, False otherwise.
        """
        if not isinstance(other, Puzzle):
            return False
        return self.difficulty < other.difficulty     

    def __eq__(self, other):
        """
        Check if two EquationPuzzle instances are equal based on their ID.

        Parameters
        ----------
        other : EquationPuzzle
            Another EquationPuzzle instance to compare with.

        Returns
        -------
        bool
            True if the puzzles are equal, False otherwise.
        """
        if not isinstance(other, Puzzle):
            return False
        return self.id == other.id 
    
    @abstractmethod
    def check_solution(self, solution):
        """
        Check whether the provided solution is correct.

        This method must be implemented by subclasses.       

        Parameters
        ----------
        solution : str
            The solution to check.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement the 'check_solution' method.")
