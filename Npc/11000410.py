""" 11000410: Venus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001731$
            # - $MyPCName$, nice to meet you!
            return 0
        elif self.index == 1:
            # $script:0831180407001732$
            # - I hope we can clean up this forest trail once more... 
            return None # TODO
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001733$
        # - This forest trail is the only path connecting us to $npcName:11000407[gender:0]$, and the monsters are making it unusable. $npcName:11000409[gender:0]$ and I are working to clear them out.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
