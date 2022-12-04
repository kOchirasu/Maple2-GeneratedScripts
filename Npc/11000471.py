""" 11000471: Vito """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002062$
        # - Ah, what is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002064$
        # - I know height isn't everything, but I really don't like being shorter than most people... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
