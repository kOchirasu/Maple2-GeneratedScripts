""" 11003088: Orde """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0207122607007930$
        # - Who would have thought places like this would still exist in Maple World?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0207122607007931$
        # - I'd love to jump into that hot spring... just not when you're watching me, $MyPCName$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
