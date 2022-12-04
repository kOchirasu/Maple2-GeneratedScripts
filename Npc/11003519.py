""" 11003519: Nimeisha """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817044507008869$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0817044507008871$
        # - Can I help you?
        if pick == 0:
            # $script:0817044507008872$
            # - Tell me about the five auras.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0817044507008873$
            # - An aura has no physical form. It's intangible. Still, if you focus hard on one thing, you're bound to reach your peak.
            return 31
        elif self.index == 1:
            # $script:0817044507008874$
            # - When you focus one gathering one type of aura, you'll feel it build up. Once it's full, it can be placed in a bowl, like water.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
