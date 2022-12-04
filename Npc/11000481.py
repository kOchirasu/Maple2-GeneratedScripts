""" 11000481: Quarry Worker """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002103$
        # - I'm busy. Why are you bothering me?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002108$
        # - I'm busy. If you're not going to help, then at least don't get in my way.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
