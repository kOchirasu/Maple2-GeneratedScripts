""" 11000637: Prisoner 140920 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002596$
        # - Get me out of here... 
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002599$
        # - Excuse me... Please get me out of here! I promise I'll never misbehave again!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
