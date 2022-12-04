""" 11003359: Ralph's Lackey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0517164307008512$
        # - You better prepare yourself.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0517164307008514$
        # - You better be ready this time. You'll see what I mean when you go inside. Heheheh...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
