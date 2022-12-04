""" 11003252: Merin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404104807008251$
        # - $MyPCName$!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0404104807008252$
        # - I'm gonna be just as awesome as you when I grow up!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
