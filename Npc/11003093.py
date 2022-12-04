""" 11003093: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0207122607007938$
        # - The Lumiknights are always watching, $MyPCName$.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0207122607007939$
        # - I'll tell you more of the Lumiknights when the time is right.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
