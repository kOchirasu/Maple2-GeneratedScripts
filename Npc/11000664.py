""" 11000664: Deke """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002699$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002701$
        # - Do you believe in love at first sight? I do. I fell in love with $npcName:11000151[gender:1]$...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
