""" 11000837: Dennis """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003064$
        # - Shush, I'm on a mission right now. Please don't interrupt me.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003067$
        # - Even the slipperiest suspect can't escape from me once I set my sights on them.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
