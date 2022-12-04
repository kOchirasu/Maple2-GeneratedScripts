""" 11001020: Clarke """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003467$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003709$
        # - I can feel time being restored to order. This means there isn't much of it left for us to spend together.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
