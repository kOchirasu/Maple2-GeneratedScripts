""" 11000795: Maritel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002960$
        # - Welcome to Cathy Mart.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002961$
        # - Is there something you're looking for? You can find everything at Cathy Mart. If we don't have it, it doesn't exist!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
