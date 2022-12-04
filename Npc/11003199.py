""" 11003199: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008226$
        # - A fight between siblings can be even more fearsome than a duel between sworn enemies. I wouldn't stand a chance if $npcName:11000069[gender:1]$ were my sister.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008227$
        # - A fight between siblings can be even more fearsome than a duel between sworn enemies. I wouldn't stand a chance if $npcName:11000069[gender:1]$ were my sister.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
