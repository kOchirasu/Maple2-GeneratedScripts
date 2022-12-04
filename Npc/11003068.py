""" 11003068: Surnuny """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102155907007655$
        # - Your Majesty...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0102155907007656$
        # - There are a great many things left to do. We should leave, for our next destination will be challenging.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
