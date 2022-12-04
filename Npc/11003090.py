""" 11003090: Orde """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0207122607007934$
        # - I guess field duty isn't that bad...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0207122607007935$
        # - It's hard to keep the Shadow Gate staffed with enough soldiers. If any more rifts like this open up, Maple World could be in serious trouble.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
