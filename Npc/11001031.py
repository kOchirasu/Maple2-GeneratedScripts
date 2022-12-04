""" 11001031: Chano """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003525$
        # - Ugh... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003528$
        # - $npcName:11000335[gender:0]$... Sigh... I don't know what to tell you about him... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
