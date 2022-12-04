""" 11004126: Fledgling Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720130407010495$
        # - ...N-nothing to report!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720130407010496$
        # - Y-you're talking to me?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
