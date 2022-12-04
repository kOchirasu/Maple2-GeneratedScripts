""" 11001060: Blanche """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 60

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180306000373$
        # - Do you have business with me?
        return None # TODO

    def __60(self, pick: int) -> int:
        # $script:0831180306000376$
        # - I don't think I'll do business with you, $MyPCName$. I prefer to work with those who have $achieve:23200015$ Trophies. I apologize for any inconvenience.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
