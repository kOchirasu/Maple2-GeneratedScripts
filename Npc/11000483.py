""" 11000483: Bunny Gal """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002119$
        # - Welcome, $MyPCName$!
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002124$
        # - You're amazing!
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407002125$
        # - You did it! Good job!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
