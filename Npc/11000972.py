""" 11000972: Sisel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003364$
        # - This situation is more serious than I thought, but I'm not going to back down now!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003366$
        # - I'll do anything for the safety and peace of $map:02000076$. I'll fight as long as I can, for the honor of the Green Hoods.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
