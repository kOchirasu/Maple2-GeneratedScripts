""" 11003261: Kaitlyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008198$
        # - Professor $npcName:11003251[gender:0]$...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008201$
        # - I've never seen Professor $npc:11003251[gender:0]$ in such a state before. I can't believe this has happened... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
