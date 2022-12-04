""" 11003185: Shadow Crow """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0510143807008458$
        # - The shadows see all.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0510145607008462$
        # - Tremble before the way of the shadow.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
