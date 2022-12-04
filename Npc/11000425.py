""" 11000425: Loki """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001772$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001774$
        # - These vultures are not tamed. What if they fly me to some unfamiliar place or drop me in midair?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
