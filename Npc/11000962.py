""" 11000962: Rhys """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003342$
        # - Things aren't as good as they used to be. Ahh well. What did you want?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003344$
        # - The Green Hoods never surrender, no matter how bad the situation is. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
