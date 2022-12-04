""" 11000256: Ren """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000402$
        # - How may I help you?
        return None # TODO

    def __1(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000406$
        # - Nothing expresses the inner YOU like carefully-selected cosmetics. How'd you like to experiment with a new look?
        if pick == 0:
            # $script:0831180610000407$
            # - Yep, time to accessorize!
            return 0
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
