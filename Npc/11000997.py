""" 11000997: Ravel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003425$
        # - Ring, ring! Out of the way!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003428$
        # - Whew, that was close. You almost startled me right off the clock!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
