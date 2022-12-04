""" 11004550: Office Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0109163907012665$
        # - This is $npcName:11004401[gender:1]$'s office. I don't know what your business is, but you watch yourself around $npcName:11004401[gender:1]$.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0109163907012666$
        # - This is $npcName:11004401[gender:1]$'s office. I don't know what your business is, but you watch yourself around $npcName:11004401[gender:1]$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
