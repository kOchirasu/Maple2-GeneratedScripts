""" 11001466: Monliver Olivieta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1223035407005524$
        # - Please put your money right here. Thank you.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1223035407005527$
        # - Don't you know who my brother is?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
