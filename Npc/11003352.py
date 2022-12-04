""" 11003352: Ralph's Lackey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0517164307008503$
        # - Get away!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0517164307008505$
        # - This time, the big guy'll mop the floor with you! No way he'll lose twice.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
