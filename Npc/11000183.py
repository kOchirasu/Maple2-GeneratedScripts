""" 11000183: Queen Bee """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000768$
        # - What izzz it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000771$
        # - Honey izz very preciouz to uzz honeybeezz! We won't let anyone take it away!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
