""" 11000009: Rolling Thunder """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000055$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000058$
            # - Have you heard of $map:02000051$? The cliffs there are so treacherous that most people wouldn't dare climb it.
            return 30
        elif self.index == 1:
            # $script:0831180407000059$
            # - If you have the chance, you should visit $map:02000051$ and visit my dad. Tell him you're $npcName:11000009[gender:0]$'s friend and you'll be like one of the family.
            if pick == 0:
                # $script:0831180407000060$
                # - Who is your father?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000061$
        # - Oh, don't worry. You'll know him when you see him.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
