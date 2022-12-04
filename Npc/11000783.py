""" 11000783: Loront """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002952$
        # - Eh? What in the world is going on?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002955$
        # - What if time never starts flowing again?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
