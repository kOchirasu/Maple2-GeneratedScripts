""" 11001568: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006056$
        # - Ah, $MyPCName$!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006111$
        # - We can't give up yet. There's still so much to do!
        return -1

    def __20(self, pick: int) -> int:
        # $script:0524142307006212$
        # - We can't give up yet. There's still too much to do!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
