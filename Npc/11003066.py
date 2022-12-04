""" 11003066: Dina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102155907007650$
        # - $MyPCName$, I'll always remember you.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0102155907007651$
        # - I was told humans were selfish, foul creatures... but in the end, a human saved me.
        if pick == 0:
            # $script:0102155907007652$
            # - How do you feel?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0102155907007653$
        # - I'll live, thanks to you. We snowcubs are strong. That's all.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
