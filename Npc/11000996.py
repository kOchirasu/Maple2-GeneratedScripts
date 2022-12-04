""" 11000996: Yodano """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003421$
        # - Speak up. I can't hear you over the alarm. Cluck!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003424$
        # - Someone, please turn off that alarm clock. Cluck!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
