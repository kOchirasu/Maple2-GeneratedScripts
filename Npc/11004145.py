""" 11004145: Vanilla """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010561$
        # - Wait!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010562$
        # - An all-expenses paid trip to Mushtopia? Count me in!  I feel like dancing!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
