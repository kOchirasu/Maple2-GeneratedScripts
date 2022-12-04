""" 11000192: Ben """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000864$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000866$
            # -  When I was young this place was a lush forest, but now it's nothing more than a sea of stumps and cabins.
            return 20
        elif self.index == 1:
            # $script:0831180407000867$
            # - Thus, "$map:02000059$." Just look around and you'll see all the empty cabins that were once occupied by loggers.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        return Option.NONE
