""" 11000588: Vincent """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1121222006000845$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1121222006000846$
        # - People with long tails are so... unusual.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
