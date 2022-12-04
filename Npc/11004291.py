""" 11004291: Everton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0921211107011344$
        # - Say the word, and I'll get it done.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0921211107011345$
        # - Shall I take your bags?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
