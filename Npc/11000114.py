""" 11000114: JJ """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000477$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000478$
        # - What if $map:02000062$ and $map:02000001$ and everything else in the world collapses?
        if pick == 0:
            # $script:0831180407000479$
            # - Don't worry.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0831180407000480$
        # - Really, $MyPCName$? Looking into this giant pit of doom doesn't fill you with the least little bit of doubt?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
