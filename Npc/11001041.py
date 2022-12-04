""" 11001041: Makrasha """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003556$
        # - How did you find this place?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003559$
        # - When I close my eyes and listen carefully, I can hear everything... Everything in the entire world.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
