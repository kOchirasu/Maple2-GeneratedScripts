""" 11000566: Ron """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002342$
        # - Go ahead. I'm listening.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002344$
        # - Stay out of trouble. You don't want to end up like Dark Wind.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
