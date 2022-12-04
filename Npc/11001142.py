""" 11001142: Meldy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0914192507003920$
        # - Uh. Hi.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0914192507003923$
        # - First the monsters start taking over the forest, and now my friends are all leaving in droves... Hmph. What do I care? I like being alone, anyway!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
