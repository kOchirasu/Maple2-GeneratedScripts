""" 11001566: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006054$
        # - Impossible... 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006109$
        # - Wake up, $npcName:11001233[gender:1]$. We still need to avenge Arazaad... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
