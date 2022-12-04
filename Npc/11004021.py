""" 11004021: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010029$
        # - I really hope Brother Junta and the expedition members get better soon.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010030$
        # - I really hope Brother Junta and the expedition members get better soon.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
