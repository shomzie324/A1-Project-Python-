"""
Chopsticks current state module
"""
from typing import List, Any
from current_state import CurrentState


class ChopsticksCurrentState(CurrentState):
    """
    Class for managing the current state of a chopsticks game

    current_value - the current value for the state of the game

    moves - possible moves based on the state of the game

    >>> ChopsticksCurrentState(True).get_possible_moves()
    ['ll', 'lr', 'rl', 'rr']

    >>> ChopsticksCurrentState(True, [0, 1, 0, 1]).is_valid_move("rr")
    True

    >>> ChopsticksCurrentState(True, [0, 1, 0, 1]).is_valid_move("ll")
    False
    """

    current_value: List[int]
    moves: List[int]

    def __init__(self, is_p1_turn: bool, value=None) -> None:
        """
        This initialize method extends the current_state initializer
        """
        self.current_value = []

        if value is None:
            CurrentState.__init__(self, is_p1_turn)
            self.current_value = [1, 1, 1, 1]
        else:
            CurrentState.__init__(self, is_p1_turn)
            self.current_value = value

        self.moves = [[], [], [], []]

        # Only populate moves if game isn't over
        if self.current_value[:2] != [0, 0] and \
                (self.current_value[1:] != [0, 0]):
            if self.get_current_player_name() == "p1":
                self._add_p1_moves()

            else:
                self._add_p2_moves()

    def __str__(self) -> str:
        """
        Return a string representation of self

        >>> print(ChopsticksCurrentState(True))
        The state is now: Player 1: 1-1; Player 2: 1-1

        >>> print(ChopsticksCurrentState(True,[3, 0, 0, 3]))
        The state is now: Player 1: 3-0; Player 2: 0-3

        >>> print(ChopsticksCurrentState(False,[0, 4, 1, 0]))
        The state is now: Player 1: 0-4; Player 2: 1-0
        """
        state = self.current_value
        return f'The state is now: Player 1: {state[0]}-{state[1]}; ' \
               f'Player 2: {state[2]}-{state[3]}'

    def _value_correction(self, move: List[int]) -> List[int]:
        """
        Correct the values of the possible move states at initialization

        >>> ChopsticksCurrentState._value_correction(ChopsticksCurrentState(True), [1, 3, 2, 6])
        [1, 3, 2, 1]

        >>> ChopsticksCurrentState._value_correction(ChopsticksCurrentState(True), [5, 3, 3, 1])
        [0, 3, 3, 1]

        >>> ChopsticksCurrentState._value_correction(ChopsticksCurrentState(True), [6, 3, 5, 4])
        [1, 3, 0, 4]
        """
        attempted_move = []

        for number in move:
            if number > 5:
                attempted_move.append(number - 5)
            elif number == 5:
                attempted_move.append(0)
            else:
                attempted_move.append(number)
        return attempted_move

    def _add_p1_moves(self) -> None:
        """
        Help method that populate moves for p1
        based on the current state of the game
        """
        if self.current_value[0] != 0 and self.current_value[2] != 0:
            # add p1 left to p2 left if p1L not dead and p2L not dead
            possible_state = self.current_value[:]
            possible_state[2] += possible_state[0]
            possible_state = self._value_correction(possible_state)
            self.moves[0] = possible_state

        if self.current_value[0] != 0 and self.current_value[3] != 0:
            # add p1 left to p2 right if p1L not dead and p2R not dead
            possible_state = self.current_value[:]
            possible_state[3] += possible_state[0]
            possible_state = self._value_correction(possible_state)
            self.moves[1] = possible_state

        # add p1 right to player 2 left if p1R and P2L not dead
        if self.current_value[1] != 0 and self.current_value[2] != 0:
            possible_state = self.current_value[:]
            possible_state[2] += possible_state[1]
            possible_state = self._value_correction(possible_state)
            self.moves[2] = possible_state

        # add p1 right to p2 right if p1R and p2R not dead
        if self.current_value[1] != 0 and self.current_value[3] != 0:
            possible_state = self.current_value[:]
            possible_state[3] += possible_state[1]
            possible_state = self._value_correction(possible_state)
            self.moves[3] = possible_state

    def _add_p2_moves(self) -> None:
        """
        Helper method that populate moves for p2
        based on the current state of the game
        """
        # add p2 left to p1 left if p2L and p1L not dead
        if self.current_value[2] != 0 and self.current_value[0] != 0:
            possible_state = self.current_value[:]
            possible_state[0] += possible_state[2]
            possible_state = self._value_correction(possible_state)
            self.moves[0] = possible_state

        # add p2 left to p1 right if p2L and p2R not dead
        if self.current_value[2] != 0 and self.current_value[1] != 0:
            possible_state = self.current_value[:]
            possible_state[1] += possible_state[2]
            possible_state = self._value_correction(possible_state)
            self.moves[1] = possible_state

        # add p2 right to p1 left if p2R and p1L not dead
        if self.current_value[3] != 0 and self.current_value[0] != 0:
            possible_state = self.current_value[:]
            possible_state[0] += possible_state[3]
            possible_state = self._value_correction(possible_state)
            self.moves[2] = possible_state

        # add p2 right  to p1 right if p2R and p1R not dead
        if self.current_value[3] != 0 and self.current_value[1] != 0:
            possible_state = self.current_value[:]
            possible_state[1] += possible_state[3]
            possible_state = self._value_correction(possible_state)
            self.moves[3] = possible_state

    def get_possible_moves(self) -> List[str]:
        """Return a list of possible moves (as letters)
        based on the current state of the game

        >>> ChopsticksCurrentState(True).get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']

        >>> ChopsticksCurrentState(True,[0, 1, 2, 4]).get_possible_moves()
        ['rl', 'rr']

        >>> ChopsticksCurrentState(False,[0, 1, 2, 0]).get_possible_moves()
        ['lr']

        >>> ChopsticksCurrentState(False,[0, 0, 2, 0]).get_possible_moves()
        []
        """
        moves = []

        if self.moves[0] != []:
            moves.append("ll")
        if self.moves[1] != []:
            moves.append("lr")
        if self.moves[2] != []:
            moves.append("rl")
        if self.moves[3] != []:
            moves.append("rr")

        return moves

    def make_move(self, move_to_make: str) -> CurrentState:
        """Apply the selected move and return
        a new CurrentState object including
        changing is_p1_turn and a new current_value (which will re populate the
        list of moves

        Because this requires input, examples not available.
        Please unit test this.
        """
        # Turn the input letters into one of the available moves
        move_state = []
        if self.get_current_player_name() == "p1":
            if move_to_make[0] == "l":
                if move_to_make[1] == "l" and self.moves[0] != []:
                    # find the move where player 1 adds their
                    # left hand value to player 2 left hand value
                    move_state = self.moves[0]
                elif move_to_make[1] == "r" and self.moves[1] != []:
                    # find the move where player 1 adds their
                    # left hand value to player 2 right hand value
                    move_state = self.moves[1]
            elif move_to_make[0] == "r":
                if move_to_make[1] == "l" and self.moves[2] != []:
                    # find the move where player 1 adds their
                    # right hand value to player 2 left hand value
                    move_state = self.moves[2]
                elif move_to_make[1] == "r" and self.moves[3] != []:
                    # find the move where player 1 adds their
                    # right hand value to player 2 right hand value
                    move_state = self.moves[3]

        elif self.get_current_player_name() == "p2":
            if move_to_make[0] == "l":
                if move_to_make[1] == "l" and self.moves[0] != []:
                    # find the move where player 2 adds their
                    # left hand value to player 1 left hand value
                    move_state = self.moves[0]
                elif move_to_make[1] == "r" and self.moves[1] != []:
                    # find the move where player 2 adds their
                    # left hand value to player 1 left hand value
                    move_state = self.moves[1]
            elif move_to_make[0] == "r":
                if move_to_make[1] == "l" and self.moves[2] != []:
                    # find the move where player 2 adds their
                    # left hand value to player 1 left hand value
                    move_state = self.moves[2]
                elif move_to_make[1] == "r" and self.moves[3] != []:
                    # find the move where player 2 adds their
                    # left hand value to player 1 left hand value
                    move_state = self.moves[3]

        # Once the string is turned into a move,
        # see if the game is over and return
        # the appropriate state
        if move_state[0] == 0 and move_state[1] == 0:
            switch_state = ChopsticksCurrentState(False, move_state)
            return switch_state
        elif move_state[2] == 0 and move_state[3] == 0:
            switch_state = ChopsticksCurrentState(True, move_state)
            return switch_state
        elif self.get_current_player_name() == "p1":
            switch_state = ChopsticksCurrentState(False, move_state)
            return switch_state
        # if game not over and p2 made the last move
        # switch to p1
        switch_state = ChopsticksCurrentState(True, move_state)
        return switch_state

    def is_valid_move(self, move: Any) -> bool:
        """
        Return true if move is in the possible

        >>> ChopsticksCurrentState(True, [1, 1, 0, 1]).is_valid_move("ll")
        False

        >>> ChopsticksCurrentState(False, [0, 1, 1, 0]).is_valid_move("rl")
        False

        >>> ChopsticksCurrentState(True, [0, 1, 1, 0]).is_valid_move("rl")
        True
        """
        return move in self.get_possible_moves()

    if __name__ == "__main__":
        import python_ta
        python_ta.check_all(config="a1_pyta.txt")
