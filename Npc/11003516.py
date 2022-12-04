""" 11003516: Jahari """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817044507008840$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0817044507008843$
        # - What?
        if pick == 0:
            # $script:0817044507008844$
            # - Tell me about the five auras.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0817044507008845$
        # - Lycaos live in the wastelands to the southwest. You can capture them to get their Enduring Health.
        if pick == 0:
            # $script:0817044507008846$
            # - Tell me about lycaos.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0817044507008847$
        # - They're not easy to capture. If you don't tie them up or stun them, they'll slip away.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
