""" 11001069: Yorke """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003643$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003646$
        # - I like groupies, so long as they don't steal my things.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
