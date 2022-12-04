""" 11004205: Mysterious Bladesman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0813101707010958$
        # - Be on your guard.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0813101707010959$
        # - There's no time to relax.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
