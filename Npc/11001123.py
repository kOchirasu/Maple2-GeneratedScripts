""" 11001123: Gerome """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0910171307003837$
        # - What seems to be the problem?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0915135007003943$
        # - The scientists in $map:2000270$ are known for their constant innovation. They're the reason I lug these heavy, expensive components everywhere I go.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
