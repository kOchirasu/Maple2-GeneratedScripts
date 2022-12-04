""" 11001597: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006085$
        # - This is my fault... 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006134$
        # - This is all my doing. I should have stayed out of $npcName:11001229[gender:0]$'s way... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
