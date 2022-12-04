""" 11001672: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0711210007006722$
        # - You have something to say to me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006893$
        # - They've pushed us all the way back to $map:63000029$...
        if pick == 0:
            # $script:0727223007006894$
            # - What's our next move?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0727223007006895$
        # - I thought we could handle this on our own, but there are too many of them. We have no choice but to report the situation to the master. He will know what to do.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
