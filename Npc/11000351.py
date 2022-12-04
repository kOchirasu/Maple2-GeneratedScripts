""" 11000351: Mirror """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 0

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000437$
        # - Just look at that gorgeous reflection! Can you believe that's you?
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (0, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
