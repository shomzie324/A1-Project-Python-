"""
Chopsticks Game Module
"""
from game import Game
from chopsticks_current_state import ChopsticksCurrentState


class ChopsticksGame(Game):
    """
    Class for playing the game chopsticks

    current_state: The current state of the Chopsticks Game
    """

    current_state: ChopsticksCurrentState

    INSTRUCTIONS_SAMPLE = "How to play Chopsticks"

    def __init__(self, is_p1_turn: bool) -> None:
        """
        This initializer extends the initilizer of the Game class
        """
        Game.__init__(self, is_p1_turn)
        self.current_state = ChopsticksCurrentState(is_p1_turn)

    def __str__(self) -> str:
        """
        Print a string representation of self

        >>> print(ChopsticksGame(True))
        Current Game: Chopsticks, Current Value: [1, 1, 1, 1]
        """
        if self.p1_turn:
            s = (f'Current Game: Chopsticks, Current Value: '
                 f'{self.current_state.current_value}')
        else:
            s = (f'Current Game: Chopsticks, Current Value: '
                 f'{self.current_state.current_value}')
        return s

    def get_instructions(self) -> str:
        """
        Return instructions for the game

        >>> ChopsticksGame(True).INSTRUCTIONS_SAMPLE in ChopsticksGame(True).get_instructions()
        True
        """
        return ("How to play Chopsticks: Each player starts with 1 "
                "finger up on each hand and the others down."
                "one player chooses one of their hands to touch "
                "the 2nd player's hand. This adds the value of their"
                "hand to the selected hand of the 2nd player. "
                "Players take turns adding to the other player's hand. "
                "When a hand reaches EXACTLY 5 that hand is dead. "
                "If the number for a hand exceeds 5 subtract 5 from "
                "the sum. When both hands are dead, that player loses!")

    def is_winner(self, player: str) -> bool:
        #  check to see if the game is over and if there are any moves available
        """
        Return True if the game is over and player is the winner

        >>> ChopsticksGame(True).is_winner("p1")
        False

        >>> ChopsticksGame(False).is_winner("P2   ")
        False
        """
        if self.is_over(self.current_state):
            return self.current_state.get_current_player_name() == (
                player.strip().lower())

        return False

    def str_to_move(self, move_to_make: str) -> str:
        # Take a string and return an int to use the legal move
        """
        Return a legal move based on the string provided

        >>> ChopsticksGame(True).str_to_move("     ll")
        'll'

        >>> ChopsticksGame(True).str_to_move("rr     ")
        'rr'

        >>> ChopsticksGame(True).str_to_move("RL")
        'rl'
        """
        return move_to_make.strip().lower()

    def is_over(self, current_state: ChopsticksCurrentState) -> bool:
        # check the current state moves list to see if any moves are possible
        # if no oves are possible the game is over
        """
        Return True if no more moves are possible

        >>> ChopsticksGame(True).is_over(ChopsticksGame(True).current_state)
        False
        """
        state_list = current_state.current_value
        if state_list[0] == 0 and state_list[1] == 0:
            return True
        elif state_list[2] == 0 and state_list[3] == 0:
            return True

        return False

    if __name__ == "__main__":
        import python_ta
        python_ta.check_all(config="a1_pyta.txt")
