""" 11000270: Gabrielle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1121222006000812$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1121222006000813$
        # - Plants will liven up your house.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
