""" 11001138: Neroa """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911192907003893$
        # - Have you seen any monsters outside?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0911192907003896$
        # - As long as I don't give up hope, all this will be behind me one day... I really wish I could believe that...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
