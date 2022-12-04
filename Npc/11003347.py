""" 11003347: Ralph's Lackey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0517164307008490$
        # - I've never met someone as strong as you.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0517164307008493$
        # - I can take you to the boss if you're lost.
        if pick == 0:
            # $script:0517164307008494$
            # - Lead the way.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # functionID=1 
        # $script:0517164307008495$
        # - Sure thing. Right this way.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
