""" 11000444: Columbo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001867$
        # - Ah... I want to get better soon, so I can go on adventures again.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001870$
        # - When can I sail again? Cough, cough! My leg had better heal quickly so I can get back to finding that pirate island.
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407001871$
        # - The sea may look calm from here, but it can destroy you in an instant.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
