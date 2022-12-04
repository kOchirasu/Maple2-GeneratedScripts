""" 11001377: Locault """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005365$
        # - Hm...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217144507005368$
        # - What, you think a woman can't be a fight manager? Just watch. I'm going to turn Boh and every other one of my clients into world champions.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
