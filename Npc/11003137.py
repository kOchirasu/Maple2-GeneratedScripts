""" 11003137: Orde """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0208220907007947$
        # - $MyPCName$, you're here!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0208220907007948$
        # - I've learned so much about the world thanks to you, $MyPCName$. Thank you so much.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
