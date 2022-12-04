""" 11001386: Ahas """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005386$
        # - Are you here to see me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1228164407005730$
        # - If the development project is a success, it'll bring wealth and fame to $map:02010063$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
