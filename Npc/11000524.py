""" 11000524: Nick """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002243$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002245$
        # - Don't sweat it. Crime is pretty bad around here. That's just how it is.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
