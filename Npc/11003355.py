""" 11003355: Ralph's Lackey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0517164307008506$
        # - It won't be so easy next time.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0517164307008508$
        # - You better get ready. The big guy'll knock your teeth out!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
