""" 11000391: Rotiana """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001589$
        # - What?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001591$
        # - Have you just arrived in $map:02000001$? I came here three days ago and I'm already sick of this city. What a waste.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
