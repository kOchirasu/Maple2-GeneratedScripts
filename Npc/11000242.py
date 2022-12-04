""" 11000242: Viola """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001023$
        # - Welcome! Ho, ho, ho.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001026$
            # - Did you come alone? Our guests usually arrive as couples. Ho, ho, ho.
            return 30
        elif self.index == 1:
            # $script:0831180407001027$
            # - Have a seat. I hope you don't feel out of place. We do get singles up here once in awhile. Sometimes they even find someone to leave with!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
