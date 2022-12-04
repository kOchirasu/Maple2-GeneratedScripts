""" 11000549: Tau """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002328$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002331$
        # - Is today some kind of holiday? Why is everyone so busy? I think I've met more people today than in my entire life.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
