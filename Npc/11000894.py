""" 11000894: Aina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003264$
        # - Everyone, wake up! We need to be alert.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003265$
        # - May the winds bring you comfort.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
