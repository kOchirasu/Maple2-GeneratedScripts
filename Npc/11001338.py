""" 11001338: Derrick """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005271$
        # - And what business do you have with a pro skater like me, hm?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005274$
        # - Hey, you want to take some pro skateboarding lessons? I teach... for a small fee.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
