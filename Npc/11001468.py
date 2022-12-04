""" 11001468: Gurio """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1223035407005532$
        # - Stop bothering me.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1223035407005535$
        # - You like my safety helmet? Two stripes from front to back is the latest fashion.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
