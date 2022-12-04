""" 11003961: Heavy Gunner """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010013$
        # - Booooring.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010014$
        # - Do you want me to teach you about the immense power of the lapenshards? ...No? Pfft.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
