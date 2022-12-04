""" 11001167: Brynn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1008163207004079$
        # - Where in the world is he?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1008163207004082$
        # - Have you seen my brother? He must be somewhere around here.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
