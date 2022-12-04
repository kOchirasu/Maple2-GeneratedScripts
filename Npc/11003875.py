""" 11003875: Miner """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0417135107009866$
        # - I-I didn't knock it over!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0417135107009867$
        # - It was a mistake!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
