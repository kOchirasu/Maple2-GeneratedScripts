""" 11004178: Katvan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010618$
        # - Do you need something?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010619$
        # - If we want to win the next match, the two of you need to be more pragmatic.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
