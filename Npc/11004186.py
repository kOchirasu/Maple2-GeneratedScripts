""" 11004186: Darphony """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010634$
        # - Ah... N-nice to meet you... 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010635$
        # - I came here to get t-t-tougher, so I can chase off the w-wolves plaguing our farm.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
