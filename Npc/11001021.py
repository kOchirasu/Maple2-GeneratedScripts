""" 11001021: Porte """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003468$
        # - Did the boss send you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003471$
        # - I don't have time for chitchat. I'm on a very important mission right now.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
