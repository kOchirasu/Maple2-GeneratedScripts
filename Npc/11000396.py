""" 11000396: Ivan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001606$
        # - Why me? What did I do?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001608$
        # - Keep those thugs away from me...
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001609$
        # - So hungry...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
