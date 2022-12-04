""" 11001455: Melatina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1222171407005450$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1222171407005453$
        # - On $map:02010022$, hard work is considered a sin. Got nothing to do? Then soak in the majesty that surrounds us!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
