""" 11004290: Plutino """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0921211107011342$
        # - Hello. How can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0921211107011343$
        # - Welcome to our fine hotel.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
