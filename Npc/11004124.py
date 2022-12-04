""" 11004124: Dark Wind Agent """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010491$
        # - The road to victory is paved with good intel.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010492$
        # - I've never seen anything so spooky.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
