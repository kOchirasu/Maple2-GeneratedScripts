""" 11000428: Hatto """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001782$
        # - Why are you bothering me?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001784$
        # - A true adventurer dives head-first into trouble! He's not afraid of jumping off a cliff into a sea of lava or fighting giant, rampaging monsters!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
