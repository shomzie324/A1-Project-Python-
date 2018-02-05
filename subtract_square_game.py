"""Substract Square Game Module

"""

from game import Game
from subtract_square_current_state import SubtractSquareCurrentState


class SubtractSquareGame(Game):
    """Game management class for subtract square game

    current_state - the current state of the game

    Because this requires input, examples not available.
    Please unit test this.
    """

    current_state: SubtractSquareCurrentState
    INSTRUCTIONS_SAMPLE = "How to play Subtract Square"

    def __init__(self, is_p1_turn: bool) -> None:
        """
        This initializer extends the initilizer of the Game class
        """
        Game.__init__(self, is_p1_turn)
        self.current_value = input("Please select a starting value:")
        while int(self.current_value) < 0:
            self.current_value = input("No Negative Numbers!"
                                       "Please select another value")
        self.current_state = (SubtractSquareCurrentState
                              (is_p1_turn, int(self.current_value.strip())))

    def __str__(self) -> str:
        """
        Print a string representation of self
        Because this requires input, examples not available.
        Please unit test this.
        """
        if self.p1_turn:
            s = f'Current Game: Subtract Square, ' \
                f'Current Value: {self.current_value}'
        else:
            s = f'Current Game: Subtract Square, ' \
                f'Current Value: {self.current_value}'
        return s

    def get_instructions(self) -> str:
        # return the instructions for the game
        """
        Return instructions for the game
        Because this requires input, examples not available.
        Please unit test this.
        """
        return ("How to play Subtract Square: Each player selects a square of"
                "a positive whole number and subtracts it"
                "from the current value until no moves are possible. "
                "Whoever was supposed to select a number when there"
                "were no possible moves left loses!")

    def str_to_move(self, move_to_make: str) -> str:
        # Take a string and return an int to use the legal move
        """
        Return a legal move based on the string provided
        Because this requires input, examples not available.
        Please unit test this.
        """
        move = move_to_make.strip()
        return move

    def is_over(self, current_state: SubtractSquareCurrentState) -> bool:
        # check the current state moves list to see if any moves are possible
        # if no oves are possible the game is over
        """
        Return True if no more moves are possible
        Because this requires input, examples not available.
        Please unit test this.
        """
        return current_state.get_possible_moves() == []

    def is_winner(self, player: str) -> bool:
        #  check to see if the game is over and if there are any moves available
        """
        Return True if the game is over and player is the winner
        Because this requires input, examples not available.
        Please unit test this.
        """
        if self.is_over(self.current_state):
            return self.current_state.get_current_player_name() == player

        return False

    if __name__ == "__main__":
        import python_ta
        python_ta.check_all(config="a1_pyta.txt")
