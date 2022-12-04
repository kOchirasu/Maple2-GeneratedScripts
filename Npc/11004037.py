""" 11004037: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010059$
        # - Even though everything's going crazy right now, it's reassuring to have you around.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010060$
        # - Even though everything's going crazy right now, it's reassuring to have you around.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
