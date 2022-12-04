""" 11000480: Kaya """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002100$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002102$
        # - $npcName:11000328[gender:0]$ has asked us to gather $itemPlural:30000055$ from the quarry in this work cart. I have no idea why he wants useless junk like this.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
