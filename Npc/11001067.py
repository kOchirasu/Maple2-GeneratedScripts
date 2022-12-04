""" 11001067: Kumier """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003634$
        # - Welcome.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407003638$
        # - Now, now. We should be laughing while we're here.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
