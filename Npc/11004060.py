""" 11004060: Pemberton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010093$
        # - The lady is heartbroken. She needs to pull herself together quickly...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010094$
        # - As the current crisis threatens all of Maple World, the Alemani family will spare no expense in addressing it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
