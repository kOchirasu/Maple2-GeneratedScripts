""" 11000353: Thompson """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001467$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001470$
            # - Our fuel needs are growing by the day. I think more excavation sites will be needed soon.
            return 30
        elif self.index == 1:
            # $script:0831180407001471$
            # - We're pumping oil every day. It's still kind of surprising how much we need to get by.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
