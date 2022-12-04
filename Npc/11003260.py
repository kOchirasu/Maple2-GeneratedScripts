""" 11003260: Lian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008196$
        # - Ah, $MyPCName$!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008197$
        # - Everyone's safe, thanks to you. I hope you won't mind if we call on your help again in the future.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
