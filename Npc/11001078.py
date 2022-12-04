""" 11001078: Luen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003679$
        # - I'm hungry.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003682$
        # - How did I never know about this place?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
