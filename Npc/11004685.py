""" 11004685: NPCNAME_11004685_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617094407015030$
        # - SCRIPTNPCNAM_0617094407015030_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0617094407015033$
        # - SCRIPTNPCNAM_0617094407015033_NAME:[F]Event
        if pick == 0:
            # $script:0617094407015034$
            # - SCRIPTNPCNAM_0617094407015034_NAME:[F]Event
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0617094407015035$
        # - SCRIPTNPCNAM_0617094407015035_NAME:[F]Event
        if pick == 0:
            # $script:0617095907015039$
            # - SCRIPTNPCNAM_0617095907015039_NAME:[F]Event
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0617094407015036$
            # - SCRIPTNPCNAM_0617094407015036_NAME:[F]Event
            return 32
        elif self.index == 1:
            # $script:0617095907015038$
            # - SCRIPTNPCNAM_0617095907015038_NAME:[F]Event
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        return Option.NONE
