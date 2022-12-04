""" 11000097: Solvay """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000381$
        # - What seems to be the problem?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000382$
        # - The Barrota Trading Company is Maple World's biggest mercantile organization. Its hawkers go everywhere in the world, no matter how steep or dangerous.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
