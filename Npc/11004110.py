""" 11004110: Oska """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010461$
        # - I'm ready for anything.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010462$
        # - The Green Hoods are always ready.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
