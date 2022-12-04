""" 11000932: Anka's Soul """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003308$
        # - Dear God of Courage, please give me strength... 
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003310$
        # - My body my be gone, but my soul still burns.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
