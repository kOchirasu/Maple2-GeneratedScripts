""" 11001054: Nomar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003600$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003603$
        # - People say that sometimes dreams, do come true. I hope they're right.
        if pick == 0:
            # $script:0831180407003604$
            # - What's your dream?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407003605$
        # - My dream isn't much. I just want to be a successful businessman. I may be delivering pizzas now, but I know I can make it big if I work hard enough.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
