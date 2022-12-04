""" 11004034: Lanemone """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010053$
        # - Sigh... How did I end up with that one again? We have unfinished business.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010054$
        # - Sigh... This one is useless without me. That's why I'm always busy cleaning up the mess. Can't really say whether or not I like it at this point.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
