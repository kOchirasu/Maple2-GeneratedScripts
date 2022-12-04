""" 11001399: Grizzle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005399$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1228164407005733$
        # - After that red sandstorm, a weird ruin popped out from the dunes. I can't wait to see what kind of secrets it holds!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
