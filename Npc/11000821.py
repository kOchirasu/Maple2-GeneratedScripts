""" 11000821: Mina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003017$
        # - Sigh...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003019$
        # - My skin is still crawling... Can I ever go back home?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
