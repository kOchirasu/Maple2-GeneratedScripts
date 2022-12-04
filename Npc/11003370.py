""" 11003370: Kyle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516225807008487$
        # - Heheheh...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0516225807008489$
        # - Savor the moment.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
