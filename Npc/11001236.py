""" 11001236: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123130907004421$
        # - Blast it...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1123130907004423$
        # - I have to stop him.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
