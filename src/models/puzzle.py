"""
Defines the abstract Puzzle base class

It defines some common attributes and methods for all puzzle types. 
Subclasses must implement the abstract method `check_solution`.

Attributes
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
    Whether the puzzle has been solved.
"""

# Make Puzzle class abstract. Subclasses must implement the abstract method 
from abc import ABC, abstractmethod

class Puzzle(ABC):
    # Construct a Puzzle object
    def __init__(self, puzzle_id, description, difficulty, max_attempts, points, attempts_made=0, is_solved=False):
        self.__id = puzzle_id
        self.__description = description
        self.__difficulty = difficulty
        self.__max_attempts = max_attempts
        self.__attempts_made = attempts_made
        self.__points = points
        self.__is_solved = is_solved

    # Getters for the puzzle attributes     
    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def get_difficulty(self):
        return self.__difficulty

    def get_max_attempts(self):
        return self.__max_attempts

    def get_attempts_made(self):
        return self.__attempts_made

    def get_points(self):
        return self.__points

    def is_solved(self):
        return self.__is_solved

    # Setters 
    def set_description(self, description):
        self.__description = description

    def set_difficulty(self, difficulty):
        if difficulty not in [1, 2, 3]:  # 1 - easy, 2 - medium, 3 - hard
            raise ValueError("Invalid difficulty level. Difficulty must be 1, 2, or 3.")
        self.__difficulty = difficulty

    def set_max_attempts(self, max_attempts):
        if max_attempts < 0:
            raise ValueError("Maximum attempts cannot be negative.")
        self.__max_attempts = max_attempts

    def set_attempts_made(self, attempts_made):
        if attempts_made < 0:
            raise ValueError("Attempts made cannot be negative")
        
        # raise an error if attempts exceed maximum attempts
        elif attempts_made > self.__max_attempts:
            raise ValueError("Attempts made cannot exceed maximum attempts.")
        self.__attempts_made = attempts_made

    def set_points(self, points):
        if points < 0:
            raise ValueError("Points cannot be negative.")
        
        self.__points = points

    def set_solved(self, is_solved):
        self.__is_solved = is_solved

    # Operator overloading - compare puzzles based on their difficlty
    def __lt__(self, other):
        return self.__difficulty < other.__difficulty
    
    # Abstract method to check if a solution is correct 
    @abstractmethod
    def check_solution(self, solution):
        pass
