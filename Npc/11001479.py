""" 11001479: Startz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0106111607005765$
        # - Do you have something to say to me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0106111607005766$
        # - I'm glad we've retrieved the Lumenstone, but the war with the Kargons is far from over.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
