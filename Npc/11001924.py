""" 11001924: Fisher """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1121140707007425$
        # - I caught a prize fish!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1121184207007436$
        # - <b>AHH!</b> I had a fish on the line, and it got away... thanks to you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
