""" 11003269: Ellie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008220$
        # - What's wrong?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008221$
        # - Platoon leader of the Green Hoods, at your service. $npcName:11000015[gender:1]$ sent me here to watch over $map:02000146$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
