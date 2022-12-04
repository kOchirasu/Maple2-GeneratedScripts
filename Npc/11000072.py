""" 11000072: Zenko """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000385$
        # - How can I help you?
        return None # TODO

    def __1(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000389$
        # - Welcome, $MyPCName$. Thinking about spicing up your look? I can give you any skin tone you like. Care to take a peek?
        if pick == 0:
            # $script:0831180610000390$
            # - Yeah, let's do it!
            return 0
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
