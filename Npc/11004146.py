""" 11004146: Mint """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010563$
        # - Mm? Are you here to see little old me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010564$
        # - Hello! It's another beautiful day in Royale Park, wouldn't you say?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
