""" 11003387: Rolling Thunder """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0719181607008677$
        # - We've got to act fast!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0719181607008678$
        # - We've got to act fast!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
