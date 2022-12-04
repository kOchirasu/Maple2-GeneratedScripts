""" 11000601: Luanna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002468$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002473$
        # - The world is relying on your strength. May the empress's blessing be with you.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1215105907009721$
        # - Empress's blessings, $MyPCName$! What brings you here?
        if pick == 0:
            # $script:1215105907009722$
            # - I've heard a lot of rumors circulating through town.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1215105907009723$
        # - Ah, yes, as have we. A dark aura begins to spread over Maple World once more.
        if pick == 0:
            # $script:1215105907009724$
            # - Tell me what you know.
            return 42
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215105907009725$
            # - I'm afraid I have no more information than anyone else. However... I sense that the strange occurrences of late are harbingers of a greater darkness. A threat unlike any we have faced.
            return 42
        elif self.index == 1:
            # $script:1215105907009726$
            # - Please... be careful.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.CLOSE
        return Option.NONE
