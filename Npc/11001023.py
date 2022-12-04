""" 11001023: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003476$
        # - No...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003477$
        # - To let him slip through my fingers... After everything he put me through...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
