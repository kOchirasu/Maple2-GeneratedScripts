""" 11004237: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0809223207010929$
        # - Good work, $MyPCName$.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0809223207010930$
            # - Good work, $MyPCName$. I'd better head back to $map:02000001$ now.
            return 10
        elif self.index == 1:
            # $script:0809223207010931$
            # - I haven't seen his face in some time.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
