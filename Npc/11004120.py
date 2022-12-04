""" 11004120: Lumiknight Mage """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010483$
        # - I'm helping $npcName:11004108[gender:0]$ research the blackshard.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010484$
        # - I'd say you yourself are worth studying, after surviving an explosion of this magnitude.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
