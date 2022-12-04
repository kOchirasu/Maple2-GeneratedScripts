""" 11001841: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1020165907007306$
        # - Ohhh... Ugh... I'm okay...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1020165907007307$
        # - Aw man. I really don't think that went super great. Why can't I be more like you?
        if pick == 0:
            # $script:1111015907007384$
            # - Maybe you need to take a break.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1020165907007308$
        # - Jeez, you think so? See, here I was thinking I gotta train harder. Otherwise, I'll never get strong enough to help you...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
