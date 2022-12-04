""" 11001378: Boh """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005369$
        # - Ugh... Who's there?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217144507005372$
        # - My head is spinning like a top... Or is it the world that's spinning? I feel like... I'm gonna die...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
