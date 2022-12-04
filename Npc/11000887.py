""" 11000887: Grinika """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003250$
        # - What do I do?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003253$
        # - Did you know Ten was a Kaka? So am I. Heh heh.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
