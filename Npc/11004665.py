""" 11004665: NPCNAME_11004665_NAME:[F]Event """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0603204607014952$
        # - SCRIPTNPCNAM_0603204607014952_NAME:[F]Event
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0603204607014953$
        # - SCRIPTNPCNAM_0603204607014953_NAME:[F]Event
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
