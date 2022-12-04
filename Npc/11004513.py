""" 11004513: Mannstad Gunner """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012469$
        # - My bullets always hit their mark!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228182607012470$
        # - My bullets always hit their mark!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
