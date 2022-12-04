""" 11004673: NPCNAME_11004673_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0603204607014976$
        # - SCRIPTNPCNAM_0603204607014976_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0603204607014977$
        # - SCRIPTNPCNAM_0603204607014977_NAME:[F]Event
        if pick == 0:
            # $script:0613033007015021$
            # - SCRIPTNPCNAM_0613033007015021_NAME:[F]Event
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0613033007015022$
        # - SCRIPTNPCNAM_0613033007015022_NAME:[F]Event
        if pick == 0:
            # $script:0613033007015023$
            # - SCRIPTNPCNAM_0613033007015023_NAME:[F]Event
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0613033007015024$
        # - SCRIPTNPCNAM_0613033007015024_NAME:[F]Event
        if pick == 0:
            # $script:0613033007015025$
            # - SCRIPTNPCNAM_0613033007015025_NAME:[F]Event
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0613033007015026$
        # - SCRIPTNPCNAM_0613033007015026_NAME:[F]Event
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
