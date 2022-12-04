""" 11003892: Turka """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009942$
        # - Hehehe...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009943$
        # - Hehehe... So you've come to me. Does that mean you're finally ready to accept my terms?
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009944$
        # - Who are you to give me orders?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
