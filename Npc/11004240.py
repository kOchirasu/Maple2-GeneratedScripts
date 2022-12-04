""" 11004240: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0809223207010940$
        # - I still feel out of sorts.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0809223207010941$
            # - I still feel out of sorts.
            return 10
        elif self.index == 1:
            # $script:0809223207010942$
            # - I am truly in your debt. Thank you. I'm sorry about everything.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
