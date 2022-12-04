""" 11001125: ABT-2XO """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0910171307003844$
        # - Entering data... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0915135007003944$
        # - Running database query on $MyPCName$... 
        #   Zero entries found in $map:2000270$ personnel list... Creating new entry.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
