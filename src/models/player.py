"""
This is the player class for the puzzle simulator.

Stores player details and manages score updates during gameplay.
"""

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

        # name must be a non-empty string
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Player name must be a non-empty string.")
        self._name = name.strip()

    @property
    def age(self):
        """Return the player's age."""
        return self._age

    @age.setter
    def age(self, age):
        """Set the player's age"""

        # must be an integer greater than 0
        if not isinstance(age, int) or age < 0:
            raise ValueError("Player age must be a non-negative integer.")
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

    def __str__(self) -> str:
        """Return the player details as a readable string."""
        return f"{self.name} (Age: {self.age}, Score: {self.score})"
