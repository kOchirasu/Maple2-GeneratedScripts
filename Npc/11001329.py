""" 11001329: Dubore """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005235$
        # - What seems to be the problem?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1217012607005238$
            # - Yesterday, 2895 guests passed on their way to $map:02010002$. Today, you are the 3527th guest.
            return 30
        elif self.index == 1:
            # $script:1227194507005707$
            # - Ah... Why can't I simply forget my useless memories? Being able to remember everything is a curse!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
