""" 11001380: Balba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005377$
        # - Mm? What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217144507005380$
        # - Who are these guys? Get them out of here! The match would already be over by now if they didn't ruin everything!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
