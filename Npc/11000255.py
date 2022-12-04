""" 11000255: Rosetta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000397$
        # - How may I help you?
        return None # TODO

    def __1(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000400$
        # - $MyPCName$, how shall we style your hair today? Anything you like, just say the word.
        if pick == 0:
            # $script:0831180610000401$
            # - Anything? Really? Well, in that case...
            return 0
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
