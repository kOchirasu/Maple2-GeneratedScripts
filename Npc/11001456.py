""" 11001456: Dolores """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1222171407005454$
        # - We just moved here.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1222171407005457$
        # - We haven't even finished unpacking, and my baby is already hurt. How dreadful!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
