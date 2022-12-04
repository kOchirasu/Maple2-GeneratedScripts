""" 11001923: Fisher """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1121140707007424$
        # - I caught a prize fish!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1121184207007433$
        # - Hey! Find your own spot!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
