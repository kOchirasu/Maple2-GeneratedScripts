""" 11003202: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008230$
        # - Jeez, who knew being a guard would be so tough?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008231$
        # - I'm learning so much just from standing in the same room as you, $MyPCName$.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0518141907008519$
        # - $MyPCName$! Something terrible has happened!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
