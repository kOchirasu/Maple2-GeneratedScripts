""" 11003440: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0721140007008688$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0721142007008706$
        # - ...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
