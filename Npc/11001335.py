""" 11001335: Tizzy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005259$
        # - Oh, wait...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005262$
        # - I forgot to return the board I rented and road it all the way home. I don't want to go all the way back to the rental place... Maybe I should just buy one for myself.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
