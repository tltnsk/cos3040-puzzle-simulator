"""
Defines the abstract Puzzle base class

The base class defines some common attributes and methods for all puzzle types. 
Subclasses must implement the abstract method check_solution.

"""

# Make Puzzle class abstract. Subclasses must implement the abstract method 
from abc import ABC, abstractmethod

class Puzzle(ABC):
    """Puzzle class"""
    def __init__(self, puzzle_id, description, difficulty, max_attempts, points, attempts_made=0, is_solved=False):
        """
        Initializes a Puzzle 
        Args:
        ---------
        __id: int
            Unique ID for the puzzle.
        __description: str
            Description of the puzzle.
        __difficulty: int
            Level of difficulty (1 - easy, 2 - medium, 3 - hard)
        __max_attempts: int
            Maximum number of attempts allowed.
        __attempts_made: int
            Number of attempts made so far.
        __points: int
            Points for solving the puzzle 
        __is_solved: bool
            Whether the puzzle has been solved or not
        """     
        self.__id = puzzle_id
        self.__description = description
        self.__difficulty = difficulty
        self.__max_attempts = max_attempts
        self.__attempts_made = attempts_made
        self.__points = points
        self.__is_solved = is_solved

    @property
    def id(self):
        """Returns the unique ID of the puzzle."""
        return self.__id

    @property
    def description(self):
        """Returns the description of the puzzle."""
        return self.__description

    @description.setter
    def description(self, description):
        """Sets the description of the puzzle."""
        self.__description = description

    @property
    def difficulty(self):
        """Returns the difficulty level of the puzzle."""
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        """Sets the difficulty level of the puzzle."""
        if difficulty not in [1, 2, 3]:  # 1 - easy, 2 - medium, 3 - hard
            raise ValueError("Invalid difficulty level. Difficulty must be 1, 2, or 3.")
        self.__difficulty = difficulty

    @property
    def max_attempts(self):
        """Returns the maximum number of attempts allowed for the puzzle."""
        return self.__max_attempts

    @max_attempts.setter
    def max_attempts(self, max_attempts):
        """Sets the maximum number of attempts allowed for the puzzle."""
        if max_attempts < 0:
            raise ValueError("Maximum attempts cannot be negative.")
        self.__max_attempts = max_attempts

    @property
    def attempts_made(self):
        """Returns the number of attempts made so far."""
        return self.__attempts_made

    @attempts_made.setter
    def attempts_made(self, attempts_made):
        """Sets the number of attempts made so far."""
        if attempts_made < 0:
            raise ValueError("Attempts made cannot be negative")
        elif attempts_made > self.__max_attempts:
            raise ValueError("Attempts made cannot exceed maximum attempts.")
        self.__attempts_made = attempts_made

    @property
    def points(self):
        """Returns the points for solving the puzzle."""
        return self.__points

    @points.setter
    def points(self, points):
        """Sets the points for solving the puzzle."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.__points = points

    @property
    def solved(self):
        """Returns whether the puzzle has been solved."""
        return self.__is_solved

    @solved.setter
    def solved(self, is_solved):
        """Sets whether the puzzle has been solved."""
        self.__is_solved = is_solved

    def __str__(self):
        """Prints the details of the puzzle."""
        return f"Puzzle {self.__id}: {self.__description} (Difficulty {self.__difficulty})"
    
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
        Checks if the provided solution is correct.

        Method must be implemented by subclasses.       

        Parameters
        ----------
        solution 
            The solution to check.

        Raises
        ------
        NotImplementedError
        If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement the 'check_solution' method.")