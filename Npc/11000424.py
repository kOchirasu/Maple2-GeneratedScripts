""" 11000424: Old Lady Balmony """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 60

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001767$
        # - What is it?
        return None # TODO

    def __60(self, pick: int) -> int:
        # $script:0831180407001771$
        # - Have you seen a lost, crying girl on the street? She's carrying a doll in her arms like it's a real baby.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
