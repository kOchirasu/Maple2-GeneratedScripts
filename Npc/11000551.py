""" 11000551: Delta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002333$
        # - Ugh... Is anyone there? 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002336$
        # - My fellow scouts have been scattered... we're on the brink... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
