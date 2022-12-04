""" 11000399: Dr. Robson """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001616$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001618$
        # - The more I think about it, the angrier I get! How could they stop me from going on vacation, and one that I've had planned for months? Maybe I should just leave and let them deal with the water.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
