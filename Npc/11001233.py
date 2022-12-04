""" 11001233: Rejan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1125194807004478$
        # - Ugh...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1125194807004481$
        # - Ugh... I was injured by a trap, and $npc:11001244[gender:0]$ ran on ahead on his own.
        if pick == 0:
            # $script:1205222707004732$
            # - What happened?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1205222707004733$
        # - We tracked $npcName:11001231[gender:0]$ and his Jibricia followers here, but they had already filled the passage with traps. I'm worried $npcName:11001244[gender:0]$ might be in danger.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
