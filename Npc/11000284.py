""" 11000284: Arwen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001109$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001112$
            # - Getting along with humans is difficult. They're just so different!
            return 30
        elif self.index == 1:
            # $script:0831180407001113$
            # - I know there are many good humans out there... but it's not easy to find them.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
