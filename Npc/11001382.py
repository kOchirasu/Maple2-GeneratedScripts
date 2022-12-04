""" 11001382: Zendal """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005382$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1228164407005727$
        # - If you're thinking of investing in $map:02010036$, you're too late... friend. I was here first.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
