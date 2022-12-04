""" 11000505: Blackstar Gangster """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002188$
        # - What brings you here?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002189$
        # - Scram, punk. 
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407002190$
        # - Who are you? Stop bothering me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
