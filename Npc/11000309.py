""" 11000309: Elvis """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1121222006000823$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1121222006000824$
        # - I dream of developing tall buildings or landmark packages.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
