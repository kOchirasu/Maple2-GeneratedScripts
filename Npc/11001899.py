""" 11001899: MC Kay """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109185407007370$
        # - Ladies and gentlemen! Are you ready for some action-packed racing?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1109185407007373$
        # - Are you joining today's race? Good luck!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
