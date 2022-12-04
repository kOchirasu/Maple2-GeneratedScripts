""" 11000251: Wei Hong """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001049$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001051$
        # - My organization is using $map:02000216$ as a foothold to expand its business to other areas. You didn't think we'd stay in the shadows forever, did you? Don't be ridiculous.  
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001052$
        # - ...Get lost.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
