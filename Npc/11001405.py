""" 11001405: Bomar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217025507005337$
        # - Sigh...
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1217025507005341$
        # - P-please don't talk to me. I d-don't know anything!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
