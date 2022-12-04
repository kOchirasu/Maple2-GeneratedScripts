""" 11001868: Rachael """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1213150207007549$
        # - Ah, nice to see you!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1213150207007551$
        # - This mine is run by the Nerman Guild. We've got all the materials a blacksmith might need.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
