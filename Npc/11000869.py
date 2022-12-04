""" 11000869: Hobb """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003142$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003144$
        # - Please don't be too loud. I can't afford any distractions from my research.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
