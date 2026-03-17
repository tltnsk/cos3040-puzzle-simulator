"""
Defines the EscapeRoom class.

Runs the game and coordinates puzzle display and scoring. 
"""
from copy import deepcopy

class EscapeRoom:
    def __init__(self, puzzles):
        self.__puzzles = deepcopy(puzzles)