""" 11004542: Keian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0110183907012678$
        # - I can't believe my luck...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0110183907012679$
            # - I can't believe my luck...
            return 10
        elif self.index == 1:
            # $script:0110183907012680$
            # - This place is <i>amazing</i>! Just this morning alone, I discovered three new molecules and a new kind of superconductor!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
