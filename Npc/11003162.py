""" 11003162: Pudge """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008070$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0306155707008073$
        # - Everyone likes flowers because they're pretty. I don't care about that, because I use them to make supplements, scented candles, and potions.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
