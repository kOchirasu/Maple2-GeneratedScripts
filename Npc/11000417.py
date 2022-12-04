""" 11000417: Sid """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1121222006000837$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1121222006000838$
        # - How may I help you?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
