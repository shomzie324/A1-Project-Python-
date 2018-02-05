"""
Current State Interface Module
"""
from typing import Any, List


class CurrentState:
    """
    Class that manages the state of the game it is contained within

    is_p1_turn - Whether or not it is player 1's turn
    current_player - The current player
    """

    is_p1_turn: bool
    current_player: str

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the state of a game
        """
        self.is_p1_turn = is_p1_turn
        if is_p1_turn:
            self.current_player = "p1"
        else:
            self.current_player = "p2"

    def __eq__(self, other: Any) -> bool:
        """
        Return true if self is equal to other
        """
        if type(self) != type(other):
            return False

        return str(self) == str(other)

    def __str__(self) -> str:
        """
        Return a string representation of self
        """
        raise NotImplementedError("Subclass Needed")

    def get_possible_moves(self) -> List[Any]:
        """
        Return a list of possible moves based on
        the current state of the game
        """
        raise NotImplementedError("Subclass Needed")

    def is_valid_move(self, move: Any) -> bool:
        """
        Return True if the attempted move is a legal move
        """
        raise NotImplementedError("Subclass Needed")

    def get_current_player_name(self) -> str:
        """
        Return a string Indicating who the current player is
        """
        return self.current_player

    def make_move(self, move_to_make: Any) -> Any:
        """
        Return a new state for the game based on the selected legal move
        """
        raise NotImplementedError("Subclass Needed")

    if __name__ == "__main__":
        import python_ta
        python_ta.check_all(config="a1_pyta.txt")
