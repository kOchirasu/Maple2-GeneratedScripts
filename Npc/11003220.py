""" 11003220: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008245$
        # - And now we're fighting literal devils...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008246$
        # - I never thought I'd miss my drill sergeant...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
