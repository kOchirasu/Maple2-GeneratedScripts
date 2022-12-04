""" 11000368: Miyo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001517$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001519$
        # - $MyPCName$, you of all people should help protect the forest!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
