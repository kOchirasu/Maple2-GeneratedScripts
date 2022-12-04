""" 11003886: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009924$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009925$
        # - What brings you here?
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009926$
        # - You seem pretty handy, considering how you handled those tasks. If only Terrun Calibre had more people like you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
