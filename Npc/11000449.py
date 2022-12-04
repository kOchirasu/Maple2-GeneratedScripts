""" 11000449: Miran """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001878$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001881$
        # - Get out of the way, I can't see $npcName:11000406[gender:0]$!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
