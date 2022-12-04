""" 11004471: Crypto """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012127$
        # - That snot-nosed brat went out to play and still hasn't come back.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1228153007012427$
            # - That snot-nosed brat went out to play and still hasn't come back.
            return 10
        elif self.index == 1:
            # $script:1227192907012128$
            # - This is no time to play. There's a war going on out there! Ugh, what would our parents say?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
