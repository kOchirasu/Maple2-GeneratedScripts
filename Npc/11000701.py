""" 11000701: Oska """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002827$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002828$
        # - We don't have time for this. I'll take $npcName:11000119[gender:0]$ to HQ.
        #   $MyPCName$, please follow $npc:11000057[gender:1]$. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
