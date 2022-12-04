""" 11004358: Evelyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011769$
        # - Oh look, $MyPCName$. Snow!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011770$
        # - I always love snow for the holidays.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
