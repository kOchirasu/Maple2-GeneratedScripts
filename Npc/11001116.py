""" 11001116: Valle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003746$
        # - What brings you to this place?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003749$
        # - Did Mom send you to bring me home? I feel bad saying this, but I can't leave yet. Not until the garden is back to normal.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
