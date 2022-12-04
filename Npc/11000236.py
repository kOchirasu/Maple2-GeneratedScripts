""" 11000236: Jerome """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001007$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001010$
        # - Don't say anything. Just go.
        if pick == 0:
            # $script:0831180407001011$
            # - What are you doing?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407001012$
        # - I said go. Geez, this is such a mess! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
