""" 11000710: Hudru """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002843$
        # - Did you call me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002846$
        # - I think I can cross this bridge if I don't look down. But... what if I lose my footing because I can't see where I'm going?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
