""" 11000609: Coye """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002504$
        # - Ah... What do I do? 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002505$
        # - What do I do if $npcName:11000526[gender:0]$'s creditors come after me? How could he hang me out to dry like this?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
