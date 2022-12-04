""" 11000365: Luchen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001508$
        # - Shush! What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001510$
        # - Shush! Please leave quietly. I'm done for if they find out I'm here. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
