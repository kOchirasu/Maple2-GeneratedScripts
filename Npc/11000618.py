""" 11000618: Jerrol """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002523$
        # - Could you help me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002524$
        # - How on the world am I supposed to fix these wagons? I can't carry them back to town!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
