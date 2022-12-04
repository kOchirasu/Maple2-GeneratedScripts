""" 11001337: Lequan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005267$
        # - You have something to say to me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005270$
        # - You here to talk, or you here to skate? Heh... Good luck.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
