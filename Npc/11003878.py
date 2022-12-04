""" 11003878: Mani """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0417135107009872$
        # - Welcome to $map:02000425$, the beautiful island of alchemy.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0417135107009873$
        # - Welcome to $map:02000425$, the beautiful island of alchemy.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0419172107009857$
        # - Welcome to $map:02000425$, the beautiful island of alchemy.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
