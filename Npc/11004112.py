""" 11004112: Mysterious Bladesman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010467$
        # - Focus on the task ahead.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010468$
        # - If you have something to say to me, say it now.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
