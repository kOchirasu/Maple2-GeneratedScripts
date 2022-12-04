""" 11004235: Blackeye """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0809223207010923$
        # - I cannot fathom how much more powerful you'll grow.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0809223207010924$
            # - I cannot fathom how much more powerful you'll grow.
            return 10
        elif self.index == 1:
            # $script:0809223207010925$
            # - It's an honor to be working by your side once more, friend.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
