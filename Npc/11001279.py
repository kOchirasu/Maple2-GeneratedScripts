""" 11001279: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1208175407004839$
        # - $npcName:11001231[gender:0]$ has struck again...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1208175407004842$
        # - We can discuss it later.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
