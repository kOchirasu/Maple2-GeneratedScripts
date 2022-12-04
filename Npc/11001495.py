""" 11001495: Startz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0118150907005816$
        # - Do you need more food?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0118150907005819$
        # - I've got a bad feeling... like something bad's about to happen.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
