""" 11003248: Strange Wall """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008163$
        # - <font color="#909090">(You feel a chill from behind the waterfall.)</font>
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008164$
        # - <font color="#909090">(Maybe there's something there... or maybe not.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
