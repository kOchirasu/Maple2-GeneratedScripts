""" 11000476: Goldus's Secretary """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002075$
        # - May I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002077$
        # - $map:02000100$ would never have been developed without the help of $npcName:11000252[gender:0]$!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
