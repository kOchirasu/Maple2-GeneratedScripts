""" 11001548: Suspicious Individual """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006395$
        # - What seems to be the problem?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0629000607006396$
        # - I've got nothing to say to you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
