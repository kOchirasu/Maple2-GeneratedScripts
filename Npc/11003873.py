""" 11003873: Huckleson """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0417135107009862$
        # - This is good enough... right?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0417135107009863$
        # - Oh, do you need help?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
