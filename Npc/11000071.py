""" 11000071: Dixon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000379$
        # - What seems to be the problem?
        return None # TODO

    def __1(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000383$
        # - Oooh, $MyPCName$, I'm so glad you found me. I can work miracles! Everyone says so. Now, what did you have in mind?
        if pick == 0:
            # $script:0831180610000384$
            # - Show me the possibilities.
            return 0
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
