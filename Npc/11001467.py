""" 11001467: Morak """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1223035407005528$
        # - Let's get to work.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1223035407005531$
        # - We have a saying in the construction industry: safety first. That means that it's none of my business if you do something stupid and get hurt!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
