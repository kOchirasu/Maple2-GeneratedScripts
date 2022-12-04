""" 11000179: Albert """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 70])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000738$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000741$
        # - $MyPCName$, huh? You have a very... fitting name.
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180407000742$
        # - Ah, we meet again. Thank you for taking care of things last time. I was able to score the contract thanks to you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        return Option.NONE
