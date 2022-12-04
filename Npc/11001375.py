""" 11001375: Bolden """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005356$
        # - Wah! You startled me!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1217144507005359$
            # - Welcome! L-look, just ignore them and keep your eyes on me, okay? Eheheh...
            return 30
        elif self.index == 1:
            # $script:1217144507005360$
            # - Eager to get out of here? Try the latest model sports car from Tuning Motors. Just start the engine and leave this dump in the dust!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
