""" 11000237: Micky """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001013$
        # - Argh, this is awful! 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001016$
        # - Hm? Why did you call me?
        if pick == 0:
            # $script:0831180407001017$
            # - What are you doing?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407001018$
        # - I don't know. Don't ask!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
