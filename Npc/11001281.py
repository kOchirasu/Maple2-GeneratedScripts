""" 11001281: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1211023307004972$
        # - Hm... Wait.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1209020507004851$
        # - I don't understand him... I really don't...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
