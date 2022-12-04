""" 11004115: Holstatt """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010473$
        # - I have no time for nonsense.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010474$
        # - Isn't there someone else you could be bothering?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
