""" 11001111: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003736$
        # - Hmm... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003737$
        # - The soul inside this orb... If it's left alone for too long, it'll be swallowed by the enormous darkness that is the Shadow World.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
