""" 11000622: Terrence """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002527$
        # - We need more people to handle the damage.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002528$
        # - Mushrooms want wooden ladders. Just wooden ones!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
