""" 11002031: Le Tierre """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 60

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180306000468$
        # - Can I help you?
        return None # TODO

    def __60(self, pick: int) -> int:
        # $script:0831180306000471$
        # - You don't live here, do you? This shop is locals only. Please shop elsewhere.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
