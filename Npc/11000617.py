""" 11000617: Marmut """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002520$
        # - This is troublesome...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002522$
        # - Hmph, I can't believe I have to investigate this!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
