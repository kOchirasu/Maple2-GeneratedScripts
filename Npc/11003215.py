""" 11003215: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008241$
        # - You've been following me. Why?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008242$
        # - I can tell you aren't one of $npcName:11000044$'s men.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
