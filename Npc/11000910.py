""" 11000910: Renji """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003272$
        # - There's nothing to life. Just let nature take its course.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003274$
        # - Stop bothering me. I don't have time for chitchat!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
