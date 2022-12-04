""" 11000390: Olson """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001585$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001587$
        # - We've been busy. People are still checking in, with no idea the empress's gathering has been canceled.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001588$
        # - The empress is no longer holding court, but we're still booked up. I don't think most people have heard the news yet.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
