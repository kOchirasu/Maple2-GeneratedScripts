""" 11000338: Mendel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001356$
        # - How can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001357$
        # - How do you think the hotel was built on this cliff? Aren't you curious? 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
