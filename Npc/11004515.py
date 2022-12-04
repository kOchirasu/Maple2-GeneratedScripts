""" 11004515: Mannstad Driver """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012475$
        # - We don't have enough fuel for our cars. We don't have enough ammo for our weapons. We just don't have enough...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1228182607012476$
            # - We don't have enough fuel for our cars. We don't have enough ammo for our weapons. We just don't have enough...
            return 10
        elif self.index == 1:
            # $script:1228182607012477$
            # - Hey, you aren't carrying any aetherine on you, are you? Ugh, as if it'd just fall into our laps like that...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
