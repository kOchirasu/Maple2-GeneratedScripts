""" 11003356: Ralph's Lackey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0517164307008509$
        # - Get away from me. I <i>really</i> don't want to talk to you.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0517164307008511$
        # - There's no way the big guy will lose to such a weakling.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
