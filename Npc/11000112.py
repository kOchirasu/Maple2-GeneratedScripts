""" 11000112: Burfy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000463$
        # - What's up?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000464$
        # - Look at this. Terrible, isn't it? Geez, I've never seen such a big fissure.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
