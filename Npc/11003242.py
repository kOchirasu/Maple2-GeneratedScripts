""" 11003242: Armano """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008142$
        # - Why'd this gotta happen to <i>me</i>?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008144$
        # - Ugh... Who are you...?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
