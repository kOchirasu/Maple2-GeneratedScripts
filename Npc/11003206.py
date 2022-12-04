""" 11003206: Mark """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008235$
        # - If it weren't for you, those thugs would have got me. I owe you.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008236$
        # - I'd be a goner if you hadn't shown up.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
