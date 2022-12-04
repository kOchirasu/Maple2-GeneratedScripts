""" 11000211: Zeta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000897$
        # - What do you want?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000899$
        # - What? Stop bothering me. Don't you have anything better to do?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
