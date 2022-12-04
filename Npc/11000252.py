""" 11000252: Chairman Goldus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001053$
        # - What do <i>you</i> want?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001055$
        # - Goldus never stops moving toward the future. There's nothing we can't make or sell.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
