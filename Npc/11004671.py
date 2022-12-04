""" 11004671: NPCNAME_11004671_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0603204607014970$
        # - SCRIPTNPCNAM_0603204607014970_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0613033007015010$
            # - SCRIPTNPCNAM_0613033007015010_NAME:[F]Event
            return 30
        elif self.index == 1:
            # $script:0613033007015011$
            # - SCRIPTNPCNAM_0613033007015011_NAME:[F]Event
            return 30
        elif self.index == 2:
            # $script:0613033007015012$
            # - SCRIPTNPCNAM_0613033007015012_NAME:[F]Event
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        return Option.NONE
