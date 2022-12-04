""" 11000872: Skan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003151$
        # - What? Do you have something to say to me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003154$
        # - Don't rely on Fairy Dew too much. This place is teeming with monsters that are stronger than you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
