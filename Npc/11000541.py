""" 11000541: Tai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002307$
        # - What's wrong?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002309$
        # - The worst thing that can happen to anyone is losing their home. It's like having the ground ripped out from under you.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407002310$
        # - An eye for an eye... I'm going to teach them what it feels like to have your life shaken to its roots.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
