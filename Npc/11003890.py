""" 11003890: Katvan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009936$
        # - It's been a while, Red Cape.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009937$
        # - It's been a while, Red Cape.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009938$
        # - I would give my life for the $npc:11003891[gender:0]$. He is the only reason I still live.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
