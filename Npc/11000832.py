""" 11000832: Whitingale """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003044$
        # - Whew, I wish I had more hands.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003046$
        # - There's no better medicine than hope. Stop being a crybaby and come over here.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
