""" 11003448: Tina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0706160807008651$
        # - The people need a reason to raise their heads up high.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0706160807008652$
        # - We're all in this together.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
