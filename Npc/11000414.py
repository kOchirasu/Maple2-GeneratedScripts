""" 11000414: Carrela """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180306000158$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1121222006000831$
        # - Spooky houses are kind of charming, really.
        return -1

    def __20(self, pick: int) -> int:
        # $script:1121222006000832$
        # - How would you like to create a haunted house?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
