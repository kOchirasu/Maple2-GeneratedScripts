""" 11003276: Old Lady Balmony """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0405160907008263$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0405160907008266$
        # - Who goes there? My eyes aren't what they used to be.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
