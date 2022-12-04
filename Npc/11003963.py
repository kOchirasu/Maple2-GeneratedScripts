""" 11003963: Runeblade """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010017$
        # - Are you versed in the way of the blade?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010018$
        # - I'd be grateful for the opportunity to speak with a peer...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
