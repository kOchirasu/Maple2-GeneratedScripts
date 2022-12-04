""" 11003351: Ralph's Lackey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0517164307008499$
        # - Taking down the boss... You're something else, you know that?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0517164307008502$
        # - The big guy's been training hard for days now. You really lit a fire under his butt, I'll tell you that.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
