""" 11000871: Tuner """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003148$
        # - Huh?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003150$
        # - $MyPCName$, would you like to know what's going on here? You look a little... bewildered.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
