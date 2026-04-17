"""
Defines the Player class.

The Player stores basic user information and user's score.
"""

class Player:
    """
    Player class
    Represents a player in the puzzle simulator.
    """

    def __init__(self, name, age):
        """
        Create a new player.

        Args
        ----------
        __name : str
            Player name.
        __age : int
            Player age.
        """
        self.__score = 0

        self.name = name
        self.age = age

    @property
    def name(self):
        """Return the player's name."""
        return self.__name

    @name.setter
    def name(self, name):
        """Set the player's name."""

        # name must be a non-empty string
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Player name must be a non-empty string.")
        self.__name = name.strip()

    @property
    def age(self):
        """Return the player's age."""
        return self.__age

    @age.setter
    def age(self, age):
        """Set the player's age"""

        # must be an integer greater than 0
        if not isinstance(age, int) or age < 0:
            raise ValueError("Player age must be a non-negative integer.")
        self.__age = age

    @property
    def score(self):
        """Return the player's score."""
        return self.__score

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
        self.__score += points

    def reset_score(self):
        """Reset the player's score to 0."""
        self.__score = 0

    def __str__(self) -> str:
        return f"{self.name} (Age: {self.age}, Score: {self.score})"