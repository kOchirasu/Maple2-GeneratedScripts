""" 11004212: Muky """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806052107010679$
        # - What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806052107010680$
        # - It's my goal in life to one day be as shroomy as the $npcName:11004213[gender:0]$. Or failing that, at least to mush it up with the best of them.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
