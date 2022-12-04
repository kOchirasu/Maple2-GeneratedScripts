""" 11004206: Dodo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0803202415009085$
        # - Mushrooms make mistakes, too...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0803202415009086$
        # - I don't feel like chatting today...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
