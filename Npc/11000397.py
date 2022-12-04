""" 11000397: Adrienne """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001610$
        # - May I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001612$
        # - It may not look it, but my house is the most expensive in the neighborhood. There's nothing quite like living up so high. I hope my daughter appreciates how hard it was for me to get this place for us.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
