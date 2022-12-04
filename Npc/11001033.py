""" 11001033: Vadell """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003533$
        # - Cough, cough... Please be careful. 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003536$
        # - Ugh... I've been holed up in here so long. My head is killing me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
