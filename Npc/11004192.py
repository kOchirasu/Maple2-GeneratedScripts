""" 11004192: Lanemone """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0813101707010952$
        # - Hmm...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0813101707010953$
        # - Hmmm... This is turning out to be pretty interesting.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
