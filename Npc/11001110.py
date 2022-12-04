""" 11001110: Marr """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003732$
        # - What's up?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003735$
        # - I knew $npcName:11000064[gender:0]$ didn't betray us!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
