""" 11003471 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817152010001894$
        # - Greetings.
        if pick == 0:
            # $script:0829173610001911$
            # - I want to go to $map:63000057$.
            return 31
        elif pick == 1:
            # $script:0829173610001913$
            # - I want to look at my daily rewards.
            return 33
        return None # TODO

    def __31(self, pick: int) -> int:
        # functionID=1 
        # $script:0817152010001901$
        # - No problem, no problem! I'll send it to you right away. Have a great time!
        return -1

    def __32(self, pick: int) -> int:
        # functionID=1 
        # $script:0817152010001902$
        # - Looking for some fun at $map:02000405$? Then off you go!
        return -1

    def __33(self, pick: int) -> int:
        # functionID=1 
        # $script:0817152010001903$
        # - I give you all these things because I care so dang much!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
