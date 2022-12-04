""" 11000402: Kiru """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001627$
        # - Uuugh... 
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001629$
        # - I need $item:20000060$ from $npcName:21000078$... to cleanse myself...
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001630$
        # - This toxin... stronger than I thought... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
