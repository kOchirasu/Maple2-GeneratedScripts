""" 11004128: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720143007010499$
        # - I'm sorry I made you worry...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720143007010500$
        # - I'm not sure how I can face everyone...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
