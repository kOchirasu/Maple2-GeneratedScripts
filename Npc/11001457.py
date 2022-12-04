""" 11001457: Klay """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1222171407005458$
        # - Nice to meet you.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1222171407005461$
        # - Coming here for my research is probably one of the best decisions I've ever made. I bet my wife and kid are happy, too.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
