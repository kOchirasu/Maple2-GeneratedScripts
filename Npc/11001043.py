""" 11001043: Aiden """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003561$
        # - This is an emergency. Whatever business you have, it can wait. 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003564$
        # - Real pros always know what to do, no matter how dire the situation is.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
