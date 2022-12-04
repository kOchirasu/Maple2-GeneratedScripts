""" 11004119: Lumiknight Warrior """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010481$
        # - I've got a mission to complete.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010482$
        # - You have our full support.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
