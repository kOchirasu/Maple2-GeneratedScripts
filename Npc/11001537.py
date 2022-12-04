""" 11001537: Ipigio """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0322222107005986$
        # - Sh! You'll give me away! 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0329103507006001$
        # - How did you find me...?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
