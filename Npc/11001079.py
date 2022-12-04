""" 11001079: Karte """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003683$
        # - I came here for brawling. Hoo, hoo, woo!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003686$
        # - Ugh... I know this isn't a vacation, but it's just too hot!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
