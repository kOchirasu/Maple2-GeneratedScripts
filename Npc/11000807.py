""" 11000807: Viata """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002975$
        # - Erm... Erm... 
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002977$
        # - The Cruel Tower is like a living hell. I don't even want to think about it. I'm lucky to have gotten out of there alive.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
