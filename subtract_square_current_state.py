"""Subtract Square Game current state module

"""
from typing import List, Any
from current_state import CurrentState


class SubtractSquareCurrentState(CurrentState):
    """
    Current State class for a subtract square game

    current_value - the current value of the game
    moves - a list of possible moves
    """

    current_value: int
    moves: List[int]

    def __init__(self, is_p1_turn: bool, current_value: int) -> None:
        """
        This initialize method extends the current_state initializer
        """
        CurrentState.__init__(self, is_p1_turn)
        self.current_value = current_value
        self.moves = []

        # formula determining values for the squares
        # elements and current value - square moves
        if self.current_value == 1:
            self.moves.append(1)

        if self.current_value > 1:
            self.moves.append(1)
            x = self.moves[-1]
            distance = 3
            next_square = x + distance
            while next_square <= current_value:
                self.moves.append(next_square)
                last_element = self.moves[-1]
                distance += 2
                next_square = last_element + distance

    def __str__(self) -> str:
        """
        Return a string representation of self

        >>> print(SubtractSquareCurrentState(True, 20))
        The current value of the game is: 20

        >>> print(SubtractSquareCurrentState(True, 50))
        The current value of the game is: 50

        >>> print(SubtractSquareCurrentState(True, 1))
        The current value of the game is: 1
        """
        return f'The current value of the game is: {self.current_value}'

    def get_possible_moves(self) -> List[str]:
        """
        Return a list of possible moves
        based on the current state of the game

        >>> SubtractSquareCurrentState(True, 20).get_possible_moves()
        ['1', '4', '9', '16']

        >>> SubtractSquareCurrentState(True, 1).get_possible_moves()
        ['1']

        >>> SubtractSquareCurrentState(False, 0).get_possible_moves()
        []
        """
        moves_2 = []
        move = sorted(self.moves)
        for x in move:
            moves_2.append(str(x))
        return moves_2

    def make_move(self, move_to_make: str) -> CurrentState:
        """
        Apply the selected move and return a new
        CurrentState object including
        changing is_p1_turn and a new current_value
        Because this requires input, examples not available.
        Please unit test this.
        """
        move_to_make = int(move_to_make)
        # make sure the player is changed properly so that it alternates
        new_value = self.current_value - move_to_make

        # if the new value is 0 i.e the game is over,
        # do not change players in the new state
        # This would mean the current player
        # made the winning move and
        # that the new state returned is the winning state
        # i.e 0 and the winning player
        if new_value == 0:
            if self.get_current_player_name() == "p1":
                new_state = SubtractSquareCurrentState(True, new_value)
            else:
                new_state = SubtractSquareCurrentState(False, new_value)

        # if new value > 0 i.e game is not over, switch players in the new state

        elif self.get_current_player_name() == "p1":
            new_state = SubtractSquareCurrentState(False, new_value)
        else:
            new_state = SubtractSquareCurrentState(True, new_value)

        return new_state

    def is_valid_move(self, move: Any) -> bool:
        """
        This method overrides the method in current_state.

        >>> SubtractSquareCurrentState(True, 20).is_valid_move(1)
        True

        >>> SubtractSquareCurrentState(True, 20).is_valid_move(25)
        False

        >>> SubtractSquareCurrentState(True, 25).is_valid_move(25)
        True
        """
        str_move = str(move)
        return str_move in self.get_possible_moves()

    if __name__ == "__main__":
        import python_ta
        python_ta.check_all(config="a1_pyta.txt")
