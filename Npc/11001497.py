""" 11001497: Tara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0118150907005824$
        # - I'm happy to be friends with such great people.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0118150907005827$
        # - I'm hoping I can relax. At least for today.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
