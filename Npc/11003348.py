""" 11003348: Ralph's Lackey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0517164307008496$
        # - This place has really transformed, thanks to you!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0517164307008498$
        # - We're all serious now. You just wait and see. The boss'll make you pay!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
