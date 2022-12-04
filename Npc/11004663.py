""" 11004663: NPCNAME_11004663_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0603204607014946$
        # - SCRIPTNPCNAM_0603204607014946_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0603204607014947$
        # - SCRIPTNPCNAM_0603204607014947_NAME:[F]Event
        if pick == 0:
            # $script:0613033007014979$
            # - SCRIPTNPCNAM_0613033007014979_NAME:[F]Event
            return 31
        elif pick == 1:
            # $script:0613033007014980$
            # - SCRIPTNPCNAM_0613033007014980_NAME:[F]Event
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0613033007014981$
            # - SCRIPTNPCNAM_0613033007014981_NAME:[F]Event
            return 31
        elif self.index == 1:
            # $script:0613033007014982$
            # - SCRIPTNPCNAM_0613033007014982_NAME:[F]Event
            return 31
        elif self.index == 2:
            # $script:0613033007014983$
            # - SCRIPTNPCNAM_0613033007014983_NAME:[F]Event
            return 31
        elif self.index == 3:
            # $script:0613033007014984$
            # - SCRIPTNPCNAM_0613033007014984_NAME:[F]Event
            return 31
        elif self.index == 4:
            # $script:0613033007014985$
            # - SCRIPTNPCNAM_0613033007014985_NAME:[F]Event
            return 31
        elif self.index == 5:
            # $script:0613033007014986$
            # - SCRIPTNPCNAM_0613033007014986_NAME:[F]Event
            return -1
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0613033007014987$
            # - SCRIPTNPCNAM_0613033007014987_NAME:[F]Event
            return 32
        elif self.index == 1:
            # $script:0613033007014988$
            # - SCRIPTNPCNAM_0613033007014988_NAME:[F]Event
            return 32
        elif self.index == 2:
            # $script:0613033007014989$
            # - SCRIPTNPCNAM_0613033007014989_NAME:[F]Event
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.NEXT
        elif (self.state, self.index) == (31, 3):
            return Option.NEXT
        elif (self.state, self.index) == (31, 4):
            return Option.NEXT
        elif (self.state, self.index) == (31, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.NEXT
        elif (self.state, self.index) == (32, 2):
            return Option.CLOSE
        return Option.NONE
