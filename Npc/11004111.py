""" 11004111: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010463$
        # - Talk to me whenever you need assistance.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010464$
        # - Our knights always do their utmost.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
