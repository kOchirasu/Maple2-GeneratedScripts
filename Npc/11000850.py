""" 11000850: Akarka """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003111$
        # - I can think. I can assess.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003114$
        # - Robots are no longer tools. We are capable of much more than our creators.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
