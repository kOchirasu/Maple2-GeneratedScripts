""" 11000963: Kamil """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003345$
        # - There are wounded people here. They need help!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003347$
        # - Folks like me don't make money sitting around on our butts. We're always on the move, looking for new buyers.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
