"""
This is the player class for the puzzle simulator.

Stores player details and manages player score updates.
"""

import re

class Player:
    """
    Player class
    Represents a player in the puzzle simulator.
    """

    def __init__(self, name, age):
        """
        Create a new player.

        Parameters
        ----------
        name : str
            Player name.
        age : int
            Player age.
        """
        self._score = 0

        self.name = name
        self.age = age

    @property
    def name(self):
        """Return the player's name."""
        return self._name

    @name.setter
    def name(self, name):
        """Set the player's name."""
        new_name = name.strip() if isinstance(name, str) else name

        # name must be a non-empty string
        if not isinstance(name, str) or new_name == "":
            raise ValueError("Name must be a non-empty string.")
        if not re.fullmatch(r"[A-Z][a-z]+", new_name):
            raise ValueError(
                "Name must start with an uppercase letter "
                "followed by lowercase letters."
            )
        self._name = new_name

    @property
    def age(self):
        """Return the player's age."""
        return self._age

    @age.setter
    def age(self, age):
        """Set the player's age"""

        # must be a valid integer greater than 0
        if isinstance(age, bool) or not isinstance(age, int) or age < 0:
            raise ValueError("Player age must be a non-negative integer.")
        if age > 120 or age < 3:
            raise ValueError("Please enter a valid age.")
        self._age = age

    @property
    def score(self):
        """Return the player's score."""
        return self._score

    def add_score(self, points):
        """
        Increase the player's score.

        Parameters
        ----------
        points : int
            Points to add (must be a non-negative integer).
        """
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a non-negative integer.")
        self._score += points

    def reset_score(self):
        """Reset the player's score to 0."""
        self._score = 0

    def __str__(self):
        """Return the player details."""
        return f"{self.name} (Age: {self.age}, Score: {self.score})"