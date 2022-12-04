""" 11000473: Bunny Gal """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002069$
        # - What is it?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002073$
        # - I don't recognize you. Is this your first time here?
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407002074$
        # - You've been staring at me. Interested?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
