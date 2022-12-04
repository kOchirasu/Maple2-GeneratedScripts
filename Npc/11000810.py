""" 11000810: Amy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002984$
        # - Sigh...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002986$
        # - $MyPCName$, I don't know how to repay you and the Lumina Liberation Army for this. Thank you so much.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
