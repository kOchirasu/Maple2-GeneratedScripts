""" 11003210: Zeta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008239$
        # - I came to repay you for saving my brother. Now we're even.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008240$
        # - Don't say I never did nothing for you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
