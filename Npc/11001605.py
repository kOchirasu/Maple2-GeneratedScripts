""" 11001605: Rejan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006093$
        # - Welcome.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006142$
        # - The sooner this is over with, the sooner I can go back to Calibre Island.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
