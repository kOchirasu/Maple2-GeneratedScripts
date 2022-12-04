""" 11003156: Pippy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008047$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0306155707008049$
        # - I know, right? All three of us are pretty, but the prettiest one is... oh, you were talking about the flowers. Sure, they're pretty too! Ah, forget what I said earlier.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
