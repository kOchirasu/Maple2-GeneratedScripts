""" 11000154: Sophia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000656$
        # - I can't get rid of these chubby cheeks, no matter how hard I try.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000659$
        # - Goodness, just LOOK at those clothes! Did you dig them out of some ancient ruins? Might be nice to wear something made in the last decade.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
