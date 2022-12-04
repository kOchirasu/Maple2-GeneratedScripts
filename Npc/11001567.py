""" 11001567: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006055$
        # - Ugh... 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006110$
        # - I'll be back on my feet... before you know it... 
        return -1

    def __20(self, pick: int) -> int:
        # $script:0524142307006211$
        # - Don't worry about me... I'll be back on my feet in no time... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
