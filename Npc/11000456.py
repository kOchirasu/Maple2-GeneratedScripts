""" 11000456: Geno """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002018$
        # - I love staying around the house.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002021$
        # - My girlfriend keeps bugging me to go out, even though it's a great day to relax inside. You get that, right? Make her see reason. If she always insists on doing... things, I worry about our future.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
