""" 11001632: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0517100407006134$
        # - Sniff... 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0517100407006135$
        # - This is all my doing... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
