""" 11003848: Condor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0117175907009811$
        # - Let's get to business.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0117175907009812$
        # - In my day, we protected the world just fine without these fancy gadgets.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
