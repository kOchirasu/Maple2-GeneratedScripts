""" 11000107: Lucy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000438$
        # - What is it?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000441$
        # - The Royal Road is blocked, and the forest path is too dangerous. I can't even go back home since the sea routes are messed up now too. I don't know what to do.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
