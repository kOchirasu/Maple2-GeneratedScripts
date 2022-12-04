""" 11003894: Black Mage """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009948$
        # - ...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009949$
        # - ...
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009950$
        # - ...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
