""" 11003265: Abandoned Notebook """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008210$
        # - <font color="#909090">(This log was tucked away in an inconspicuous corner.)</font>
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008211$
        # - <font color="#909090">(It looks like this was abandoned, and yet it's suspiciously free of dust.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
