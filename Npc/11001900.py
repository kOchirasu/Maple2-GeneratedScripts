""" 11001900: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1122193107007458$
        # - Eve was right...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1122193107007461$
        # - We've got to hold out long enough for Eve to get reinforcements.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
