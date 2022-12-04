""" 11004672: NPCNAME_11004672_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0603204607014973$
        # - SCRIPTNPCNAM_0603204607014973_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0613034407015027$
        # - SCRIPTNPCNAM_0613034407015027_NAME:[F]Event
        if pick == 0:
            # $script:0613034407015028$
            # - SCRIPTNPCNAM_0613034407015028_NAME:[F]Event
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0613033007015015$
        # - SCRIPTNPCNAM_0613033007015015_NAME:[F]Event
        if pick == 0:
            # $script:0613034407015029$
            # - SCRIPTNPCNAM_0613034407015029_NAME:[F]Event
            return 32
        elif pick == 1:
            # $script:0613033007015017$
            # - SCRIPTNPCNAM_0613033007015017_NAME:[F]Event
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # $script:0613033007015018$
        # - SCRIPTNPCNAM_0613033007015018_NAME:[F]Event
        return -1

    def __33(self, pick: int) -> int:
        # $script:0613033007015019$
        # - SCRIPTNPCNAM_0613033007015019_NAME:[F]Event
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
