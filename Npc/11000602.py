""" 11000602: Tarre """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002479$
        # - Ugh... What... brings you... to me?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002481$
        # - P-please go... I'll be okay... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
