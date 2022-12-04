""" 11004669: NPCNAME_11004669_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0603204607014964$
        # - SCRIPTNPCNAM_0603204607014964_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0603204607014966$
            # - SCRIPTNPCNAM_0603204607014966_NAME:[F]Event
            return 30
        elif self.index == 1:
            # $script:0613033007015002$
            # - SCRIPTNPCNAM_0613033007015002_NAME:[F]Event
            if pick == 0:
                # $script:0613033007015003$
                # - SCRIPTNPCNAM_0613033007015003_NAME:[F]Event
                return 31
            elif pick == 1:
                # $script:0613033007015004$
                # - SCRIPTNPCNAM_0613033007015004_NAME:[F]Event
                return 32
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0613033007015005$
        # - SCRIPTNPCNAM_0613033007015005_NAME:[F]Event
        return -1

    def __32(self, pick: int) -> int:
        # $script:0613033007015006$
        # - SCRIPTNPCNAM_0613033007015006_NAME:[F]Event
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
