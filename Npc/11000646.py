""" 11000646: Prisoner 160919 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002642$
        # - Get me out of here... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002645$
        # - It's been three days since the toilet overflowed...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
