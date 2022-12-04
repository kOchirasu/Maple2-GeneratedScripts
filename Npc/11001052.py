""" 11001052: Alicia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003592$
        # - Wah... I messed it up!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003595$
        # - No one can imagine how exciting time travel is without trying it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
