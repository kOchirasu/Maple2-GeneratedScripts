""" 11004437: Nairin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1213154907011978$
        # - Would you like to take on a mission for Green Hoods?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1213154907011979$
        # - Where should I start? Local ecology? Demographics? There's so much data to collate!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
