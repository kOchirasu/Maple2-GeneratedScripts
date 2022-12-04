""" 11004438: Mason """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1213154907011980$
        # - It is time my order stood with the rest of the empire.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1213154907011981$
        # - So many fantastic riddles await us in Kritias... It's exhilarating.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
