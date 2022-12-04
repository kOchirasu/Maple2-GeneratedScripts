""" 11004670: NPCNAME_11004670_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0603204607014967$
        # - SCRIPTNPCNAM_0603204607014967_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0613033007015007$
            # - SCRIPTNPCNAM_0613033007015007_NAME:[F]Event
            return 30
        elif self.index == 1:
            # $script:0613033007015008$
            # - SCRIPTNPCNAM_0613033007015008_NAME:[F]Event
            return 30
        elif self.index == 2:
            # $script:0613033007015009$
            # - SCRIPTNPCNAM_0613033007015009_NAME:[F]Event
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
