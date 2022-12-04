""" 11001243: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1203181207004683$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1203181207004686$
        # - Now that the draft is in place, we'd better hurry back to the fortress.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
