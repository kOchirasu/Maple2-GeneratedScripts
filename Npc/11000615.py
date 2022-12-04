""" 11000615: Kent """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002514$
        # - Huh?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002516$
        # - The empire turned its back on these people when they needed it the most. Someone had to step in and protect them. And the empire will get what it deserves.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
