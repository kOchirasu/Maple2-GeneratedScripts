""" 11001500: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0118150907005836$
        # - What do I want to eat this time?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0118150907005839$
        # - Could you stop bothering me? I'm eating!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
