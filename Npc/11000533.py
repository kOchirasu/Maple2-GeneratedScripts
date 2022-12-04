""" 11000533: Camton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002298$
        # - What seems to be the problem?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002300$
        # - Unless you've worked a day here, you can't truly appreciate what we're doing.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
