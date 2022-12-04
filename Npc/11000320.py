""" 11000320: Lyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001250$
        # - What is it?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001254$
        # - Everyone thinks they're special, but the world keeps turning without them.
        if pick == 0:
            # $script:0831180407001255$
            # - What's wrong?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001256$
            # - Nothing. I just understand the way of the world.
            return 41
        elif self.index == 1:
            # $script:0831180407001257$
            # - Dust thou art, and to dust shalt thou return. Come empty, return empty. In the end, there's nothing in this world that is truly yours.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.CLOSE
        return Option.NONE
