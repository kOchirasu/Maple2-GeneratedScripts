""" 11001047: Reker """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003578$
        # - This has been a perfect misjudgment.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003581$
        # - Everyone at  Goldus Industries is a real smooth talker. They say they care about us workers, but if they did we wouldn't be having any problems, would we?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
