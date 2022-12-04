""" 11000502: Armano """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002182$
        # - Why did you call me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002183$
        # - I want to go home... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
