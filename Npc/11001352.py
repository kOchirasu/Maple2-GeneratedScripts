""" 11001352: Wei Hong """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005320$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005323$
        # - Heh. This place isn't as big a dump as I thought it'd be.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
