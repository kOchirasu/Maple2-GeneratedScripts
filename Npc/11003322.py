""" 11003322: Soldier """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0424104307008425$
        # - What seems to be the problem?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0424104307008426$
        # - The enemy is up to something.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
