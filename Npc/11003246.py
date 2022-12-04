""" 11003246: Frey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008152$
        # - $MyPCName$.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008153$
        # - In times like this, you need to keep your wits about you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
