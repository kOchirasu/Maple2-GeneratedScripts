""" 11003263: Jorge """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008206$
        # - $MyPCName$... You did everything you could.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008207$
        # - The path to Ellinel is still blocked, but we'll find a way back.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
