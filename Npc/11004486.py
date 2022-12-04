""" 11004486: Vivipara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012275$
        # - Hey, you're from Maple World, right?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012276$
        # - Hey, you're from Maple World, right?
        if pick == 0:
            # $script:1227192907012277$
            # - Is something wrong?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012278$
            # - Everything's wrong! I loathe field work. Everything around here wants to tombstone me. And it's been days since I had a proper bath! This assignment must be a sick joke on the part of my boss.
            return 11
        elif self.index == 1:
            # $script:1227192907012279$
            # - I miss my lab in Tria. I hope this mission ends soon...
            if pick == 0:
                # $script:1227192907012280$
                # - Cheer up!
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:1227192907012281$
        # - I hadn't thought of it that way. Thank you. You cheer up, too!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
