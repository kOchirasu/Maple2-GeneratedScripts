""" 11000372: Dr. Mikhail """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001526$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001529$
        # - As scientists, we must always look toward the future. We must not abandon our research because we aren't happy with the immediate results, or out of fear of perceived consequences. Science requires persistence and dedication!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
