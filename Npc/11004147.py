""" 11004147: Ralph """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010565$
        # - What do you want?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010566$
        # - This place is gonna make me rich! I've just gotta figure out how, first...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
