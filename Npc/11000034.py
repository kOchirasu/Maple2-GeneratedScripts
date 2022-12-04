""" 11000034: Mahio """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000189$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000191$
        # - Nothing's more important than peace of mind. I find mine snuggled up safe in bed.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
