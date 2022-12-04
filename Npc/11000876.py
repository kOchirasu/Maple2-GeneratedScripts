""" 11000876: Belhi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003184$
        # - Do you know how the fairfolk greet each other?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003186$
        # - Forests are the cradle of life for woodland creatures like us fairfolk. If they get cut down, we'll fall with them.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
