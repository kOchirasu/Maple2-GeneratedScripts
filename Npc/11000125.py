""" 11000125: Benjamin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000540$
        # - How did it come to this?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000542$
        # - I've got to determine whether the mutated DNA strand was an outside contaminant, or was somehow mistakenly synthesized inside our test subjects...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
