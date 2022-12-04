""" 11001103: Rute """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180306000404$
        # - You must be here to see me.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0809123006000906$
        # - The stuff's not ready yet. Come back later.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
