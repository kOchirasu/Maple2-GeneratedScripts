""" 11000477: Praise Goldus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002078$
        # - There's a name on it: $npcName:11000477$.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002079$
        # - The Goldus way! Put your back into it! Pinch a penny, make a penny!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
