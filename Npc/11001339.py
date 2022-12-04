""" 11001339: Potler """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005275$
        # - Skateboarding is harder than it looks.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005278$
        # - Why is this so hard?! I can <i>visualize</i> myself doing these tricks, so why can't I actually <i>do</i> them?!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
