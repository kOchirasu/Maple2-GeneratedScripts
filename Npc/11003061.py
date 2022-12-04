""" 11003061: Frozen Tree """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102155907007643$
        # - <font color="#909090">(A chilling wind blows through the gap in the ice wall behind the frozen tree.)</font>
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0102155907007644$
        # - <font color="#909090">(Something must be hidden behind this tree.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
