""" 11000619: Janne """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002525$
        # - Try to think positively.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002526$
        # - It's nice to be outside sometimes.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
