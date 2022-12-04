""" 11001074: Allison """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003663$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003666$
        # - Every single picture here is drawn by a child. Amazing, right?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
