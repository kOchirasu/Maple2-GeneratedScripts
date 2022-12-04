""" 11003153: Rudy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008035$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0306155707008038$
        # - $MyPCName$, did you come to enjoy the flowers? So did I!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
