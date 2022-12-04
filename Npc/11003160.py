""" 11003160: Mindy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008063$
        # - Oh, hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0306155707008066$
        # - I don't think anyone hates flowers, right? Everyone has to have a favorite flower or two.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
