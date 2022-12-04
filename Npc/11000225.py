""" 11000225: Old Man Maneux """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000979$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000982$
        # - Love isn't just about being with someone. Sometimes it's about their memory, too...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
