""" 11001579: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006067$
        # - Ah, $MyPCName$!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006121$
        # - This is not going to be easy. 
        return -1

    def __20(self, pick: int) -> int:
        # $script:0524142307006215$
        # - This is not going to be easy. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
