""" 11001025: Eve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003479$
        # - Ah... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003482$
        # - It's not over until we catch $npcName:11000044[gender:0]$. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
