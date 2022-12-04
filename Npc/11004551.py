""" 11004551: Office Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0109163907012668$
        # - You! Outlander! You better not be here to bother $npcName:11004401[gender:1]$.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0109163907012669$
        # - You! Outlander! You better not be here to bother $npcName:11004401[gender:1]$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
