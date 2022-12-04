""" 11004107: Pemberton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010455$
        # - I am dutybound to protect the young mistress.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010456$
        # - For the lady, I would sacrifice anything.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
