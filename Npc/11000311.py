""" 11000311: Isaac """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1121222006000825$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1121222006000826$
        # - I'm going to be rich, no matter what it takes!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
