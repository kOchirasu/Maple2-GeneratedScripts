""" 11001071: Damon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003651$
        # - Are you sure you came to see me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003654$
        # - The streets here look like a jungle.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
