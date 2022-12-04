""" 11000350: Jeremy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001460$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001462$
        # - I've been traveling all my life, and the greatest lesson I've learned is to never waste anything. $npcName:21000029$, for example, has hundreds of practical uses. It's amazing stuff!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
