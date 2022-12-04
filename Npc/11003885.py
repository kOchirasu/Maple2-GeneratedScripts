""" 11003885: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009921$
        # - Our investigation continues.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009922$
        # - Our investigation continues.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009923$
        # - Thank you. I think I've started to unravel the truth.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
