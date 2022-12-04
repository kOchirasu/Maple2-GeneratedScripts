""" 11000447: Injured Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 80

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001872$
        # - Ugh...
        return None # TODO

    def __80(self, pick: int) -> int:
        # $script:0831180407001877$
        # - Ugh...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (80, 0):
            return Option.CLOSE
        return Option.NONE
