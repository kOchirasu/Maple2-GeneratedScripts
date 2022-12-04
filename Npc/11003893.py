""" 11003893: Madria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009945$
        # - Why is the $npc:11003894[gender:0]$ constantly calling meetings? What a chore!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009946$
        # - Why is the $npc:11003894[gender:0]$ constantly calling meetings? What a chore!
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009947$
        # - Gah, I'm so bored. I want to head back to the castle soon.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
