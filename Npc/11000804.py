""" 11000804: Liam """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002962$
        # - Do you have something to say to me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002965$
        # - $MyPCName$, never let your guard down. Not for an instant. You're a long way from Maple World.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
