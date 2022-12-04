""" 11000643: Prisoner 150125 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002624$
        # - Get me out of here... 
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002628$
        # - Argh, this place is a sty! I hate prison! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
