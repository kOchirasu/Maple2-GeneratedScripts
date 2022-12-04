""" 11000616: Maroon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002517$
        # - What seems to be the problem?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002519$
        # - Don't compare us to the empire. They care more about their hierarchy than the safety of their charges. Their hypocrisy is disgusting.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
