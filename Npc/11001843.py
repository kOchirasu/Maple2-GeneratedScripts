""" 11001843: Eks """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1020165907007310$
        # - My head... My shoulders... My spleen...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1020165907007311$
        # - The room's spinning. Who knows when I'll be ready for active duty?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
