""" 11000784: Carrie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002956$
        # - Who are you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002959$
        # - Strange... I see cake everywhere, but I smell nothing.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
