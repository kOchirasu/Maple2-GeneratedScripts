""" 11000036: Arita """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000196$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000199$
        # - Love the flowers and trees as you love yourself. Without them, you wouldn't exist.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
