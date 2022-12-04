""" 11003141: Rina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0222124707007953$
        # - What's the matter, dear?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0224093607007962$
        # - Cooking in the kitchen is fine, but I'll always prefer cooking outdoors for how liberating it feels.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
