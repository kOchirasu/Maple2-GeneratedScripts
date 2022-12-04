""" 11000961: Tinnie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003339$
        # - Why can't I shake this bad feeling...?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003341$
        # - One day, I want to follow in $npcName:11000015[gender:1]$'s footsteps and become the leader of the Green Hoods. I want to earn the same respect that she did.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
