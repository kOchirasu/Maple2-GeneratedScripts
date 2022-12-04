""" 11000151: Cecilia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000644$
        # - What?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000645$
        # - Out of my way.
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407000646$
        # - Go ask yourself.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        return Option.NONE
