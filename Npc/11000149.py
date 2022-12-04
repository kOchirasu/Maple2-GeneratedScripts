""" 11000149: Collin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000635$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000637$
        # - Have you seen a puppy around here?
        if pick == 0:
            # $script:0831180407000638$
            # - Nope.
            return 21
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407000639$
        # - Ahhh... Whitey, where are you? I should never have taken him outside. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        return Option.NONE
