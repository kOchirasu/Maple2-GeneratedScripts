""" 11000135: Squattush """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000559$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000561$
        # - Shush! Lower your voice.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
