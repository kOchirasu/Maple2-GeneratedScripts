""" 11001490: Ereve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0114152507005802$
        # - $MyPCName$, what brings you to me?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0114152507005804$
        # - It was no small task to recover the power of light. I pray it will never be overshadowed by darkness.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
