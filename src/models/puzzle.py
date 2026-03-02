"""
Defines the abstract Puzzle base class
"""

from abc import ABC, abstractmethod

class Puzzle(ABC):
    def __init__(self, puzzle_id, description, difficulty, max_attempts, points, attempts_made=0, is_solved=False):
        self.__id = puzzle_id
        self.__description = description
        self.__difficulty = difficulty
        self.__max_attempts = max_attempts
        self.__attempts_made = attempts_made
        self.__points = points
        self.__is_solved = is_solved

    # Getters    

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
        elif attempts_made > self.__max_attempts:
            raise ValueError("Attempts made cannot exceed maximum attempts.")
        self.__attempts_made = attempts_made

    def set_points(self, points):
        if points < 0:
            raise ValueError("Points cannot be negative.")
        
        self.__points = points

    def set_solved(self, is_solved):
        self.__is_solved = is_solved

    # Operator overloading 
    def __lt__(self, other):
        return self.__difficulty < other.__difficulty
    
    # Abstract method 
    @abstractmethod
    def check_solution(self, solution):
        pass
