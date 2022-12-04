""" 11001969: Ereve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0201161807007915$
        # - Welcome, $MyPCName$.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0201161807007916$
        # - $MyPCName$, I'm looking forward to hearing more great stories of your heroism.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
