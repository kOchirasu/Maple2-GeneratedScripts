""" 11001099: Oska """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003697$
        # - Hmm... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003698$
        # - This place is $map:52000011$. It channels the power of the Red Lapenta to maintain order among the timelines.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
