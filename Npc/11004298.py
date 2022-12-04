""" 11004298: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011381$
        # - Clean clean clean... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1002141907011384$
        # - It's my job to keep this hotel clean, and I'm darn good at it! Except... there's this one thing I can't seem to tidy up!
        if pick == 0:
            # $script:1002141907011385$
            # - What might that be?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011386$
        # - Over there, in the sofa by the window. There are papers stuck in there that I can't seem to get loose. Did someone put those there on purpose? 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
