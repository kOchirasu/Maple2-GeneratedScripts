""" 11000868: Tess """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003139$
        # - Oh?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003141$
        # - Are they doing this to me because I'm an intern? I didn't become a researcher to run errands!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
