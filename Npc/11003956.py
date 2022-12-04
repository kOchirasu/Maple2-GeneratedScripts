""" 11003956: Priest """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010003$
        # - Do you believe in the power of the light?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010004$
        # - This Frontier Foundation is a beautiful place. I look forward to working with such capable individuals.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
