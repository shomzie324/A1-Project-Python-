"""Module for game superclass

"""
from typing import Any


class Game:
    """
    Superclass for games that can be used by game_interface

    is_p1_turn - whether or not it is player 1's turn
    """

    is_p1_turn: bool

    def __init__(self, is_p1_turn: bool) -> None:
        self.p1_turn = is_p1_turn

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other):
            return False
        return self is other

    def __str__(self) -> str:
        raise NotImplementedError("Subclass Needed")

    def get_instructions(self) -> str:
        """
        Return a string explaining the instructions for the game
        """
        raise NotImplementedError('Subclass Needed')

    def is_winner(self, player: str) -> bool:
        """
        Return True if the string player is the winner of the game
        """
        raise NotImplementedError("Subclass Needed")

    def str_to_move(self, move_to_make: str) -> Any:
        """
        Return a move for the game based on its input string representation
        """
        raise NotImplementedError('Subclass Needed')

    def is_over(self, current_state: Any) -> bool:
        """
        Return True if the game is over
        """
        raise NotImplementedError("Subclass Needed")

    if __name__ == "__main__":
        import python_ta
        python_ta.check_all(config="a1_pyta.txt")
