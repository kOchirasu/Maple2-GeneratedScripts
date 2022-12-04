""" 11000973: Hamantha """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003367$
        # - Oh, no. You aren't getting my digits. Now shoo!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003369$
        # - Sniff... Name's $npcName:11000973[gender:1]$, and I'm the prettiest little thing you're going to find in $map:02000186$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
