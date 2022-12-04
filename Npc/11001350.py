""" 11001350: Oliver Olivieta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005313$
        # - Good. Right. Perfect!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005316$
        # - Yeeees? It's rude to barge in on someone's summer home, you know. Please remove yourself from the premises.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
