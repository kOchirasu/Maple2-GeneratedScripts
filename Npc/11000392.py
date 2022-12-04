""" 11000392: Timus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001592$
        # - Huh?
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001594$
            # - Did you hear the court was canceled? I thought it would be a big to-do, so I arrived two weeks ago.
            return 20
        elif self.index == 1:
            # $script:0831180407001595$
            # - And now it's canceled! Argh, I stayed at the hotel for two weeks for nothing!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        return Option.NONE
