""" 11000182: Junkyard Worker """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000762$
        # - What?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407000767$
        # - Scram, I got work to do.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
