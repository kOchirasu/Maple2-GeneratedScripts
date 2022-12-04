""" 11003872: Bedd """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0417135107009860$
        # - What's more important? The process? Or the results?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0417135107009861$
        # - I guess you need good process <i>and</i> solid results.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
