""" 11001379: Zenka """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005373$
        # - You called?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217144507005376$
        # - Where in the world did they come from? Of course they chose <i>today</i> to cause a mess. When the dust clears, it'll be us security guards who take the fall for this.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
