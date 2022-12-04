""" 11000405: Dark Wind Bulletin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001640$
        # - This is the Dark Wind Bulletin Board.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001641$
        # - Eliminate $npcName:29000023$ and bring me proof for your reward.
        #   - Captain $npcName:11000044[gender:0]$
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
