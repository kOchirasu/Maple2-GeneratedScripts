""" 11000129: Alvin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000552$
        # - What seems to be the problem?
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000555$
            # - I took the Royal Road for granted. I've never been on a path so dangerous before. 
            return 40
        elif self.index == 1:
            # $script:0831180407000556$
            # - And even if you get through this awful forest, there's a treacherous valley to cross. The cliffs of $map:02000051$ are nothing compared to what's ahead! Ahh, I'm never getting out of here alive...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
