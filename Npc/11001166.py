""" 11001166: Merin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1008163207004068$
        # - What should I do?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1008163207004071$
        # - Shh! Please, keep your voice down! <i>That mage</i> can't know I'm here!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
