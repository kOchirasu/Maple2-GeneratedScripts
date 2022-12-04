""" 11000115: Elly """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000483$
        # - What is it?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000487$
        # - Hmph! Just as well. I hope the road stays destroyed forever.
        if pick == 0:
            # $script:0831180407000488$
            # - Why's that?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407000489$
        # - Smith left for $map:02000001$ to see the court instead of staying with me for my birthday. I don't need a boyfriend who cares more about the empress than me. I hope he'll never come back. Hmph!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
