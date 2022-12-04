""" 11000635: Prisoner 140918 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002582$
        # - Get me out of here... 
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002585$
            # - Another tourist? Come to see all the animals in their cages?
            if pick == 0:
                # $script:0831180407002586$
                # - How did you end up in here?
                return 31
            return 30
        elif self.index == 1:
            # $script:0831180407002588$
            # - Ugh... This smell... The toilet is clogged...
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407002587$
        # - For swearing. Why? Don't say you never swear. Everyone does it! So why is it such a crime??
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
