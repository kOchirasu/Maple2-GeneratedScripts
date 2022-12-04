""" 11003094: Blackeye """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0207122607007940$
        # - Ahh it's you, $MyPCName$.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0207122607007941$
        # - Dark Wind is changing. It's not the same organization you once knew.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
