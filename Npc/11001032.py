""" 11001032: Herman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003529$
        # - This is bad, really bad!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003532$
        # - I'm the head of this robot development center, and even I don't know how to get these robots under control. What should I do to contain this problem?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
