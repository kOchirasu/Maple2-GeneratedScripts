""" 11001075: Mojiran """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003667$
        # - Wah! You startled me.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003670$
        # - Ah, I came here on a tour...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
