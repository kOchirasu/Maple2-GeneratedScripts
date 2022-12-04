""" 11003208: Zeta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008237$
        # - Thank you for saving my brother!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008238$
        # - I thought my bro was a goner... until you came along, that is.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
