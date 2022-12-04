""" 11001300: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005014$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1215203907005017$
        # - I command the Royal Knights of Empress $npcName:11000075[gender:1]$. Her safety is our duty.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
