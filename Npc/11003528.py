""" 11003528: Small Hut """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816165015009054$
        # - (It's locked.)
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816165015009055$
        # - (It's locked.)
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
