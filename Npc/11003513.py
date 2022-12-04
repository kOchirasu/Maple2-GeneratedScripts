""" 11003513: Latisha """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817044507008806$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0817044507008809$
        # - What brings you here?
        if pick == 0:
            # $script:0817044507008810$
            # - Tell me about the five auras.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0817044507008811$
        # - The Vayar live in the mountains to the northeast. Break a Vayar apart, and you'll get some Steadfast Will. It isn't easy...
        if pick == 0:
            # $script:0817044507008812$
            # - Tell me about the Vayar.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0817044507008813$
        # - They're solid. And tough. Magic doesn't work on them, either. You've got to fight them up close!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
