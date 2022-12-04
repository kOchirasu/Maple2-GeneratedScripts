""" 11001521: Archer """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515211707006109$
        # - Nice to meet you!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515211707006110$
        # - I didn't expect $map:02000023$ to be quite this beautiful. When the boss told me the Green Hoods were joining this mission, I didn't know what to think. I've never been so far from home before... But I promise I won't let you down!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
