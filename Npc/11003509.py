""" 11003509: Troe """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009014$
        # - Ah... Hello...?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115009015$
        # - Ah... Hello...? I want to make some monster friends...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
