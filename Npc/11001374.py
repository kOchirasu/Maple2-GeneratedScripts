""" 11001374: Dortov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005352$
        # - Hm...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217144507005355$
        # - I don't care <i>why</i> this place is in shambles. I care that these noisy hooligans are preventing me from doing my job!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
