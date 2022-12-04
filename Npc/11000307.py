""" 11000307: Arnold """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1121222006000819$
        # - Welcome. What brings you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1121222006000820$
        # - Everyone needs a place to call home.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
