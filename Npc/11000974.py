""" 11000974: Mani """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003370$
        # - Welcome, and thank you for coming all the way here.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003372$
        # - It gives me tremendous pleasure to watch people enjoying my food. Ho, ho!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
