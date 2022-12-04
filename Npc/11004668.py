""" 11004668: NPCNAME_11004668_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0603204607014961$
        # - SCRIPTNPCNAM_0603204607014961_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0613033007014996$
        # - SCRIPTNPCNAM_0613033007014996_NAME:[F]Event
        if pick == 0:
            # $script:0613033007014997$
            # - SCRIPTNPCNAM_0613033007014997_NAME:[F]Event
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0613033007014998$
        # - SCRIPTNPCNAM_0613033007014998_NAME:[F]Event
        if pick == 0:
            # $script:0613033007014999$
            # - SCRIPTNPCNAM_0613033007014999_NAME:[F]Event
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0603204607014962$
        # - SCRIPTNPCNAM_0603204607014962_NAME:[F]Event
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
