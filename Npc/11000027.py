""" 11000027: Corni """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000175$
        # - Yes? Yes? What do you need? How can I help?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000177$
        # - I messed up. I messed it all up. Woe is meee!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
