""" 11003192: Kyle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0405160907008256$
        # - Heh heh heh...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0405160907008258$
        # - What brings you here?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
