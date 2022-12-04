""" 11004457: Evian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0109134107012662$
        # - Our first steps in a new world. I should be excited, but all I feel is nervous...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0109134107012663$
        # - Our first steps in a new world. I should be excited, but all I feel is nervous...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
