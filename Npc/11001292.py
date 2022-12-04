""" 11001292: Startz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005006$
        # - Cooking requires focus. Understand?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1230171207005752$
        # - Order now or get a face full of burning oil. Your choice. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
