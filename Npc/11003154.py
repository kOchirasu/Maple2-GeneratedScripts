""" 11003154: Ruly """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008039$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0306155707008042$
        # - If you're troubled, come look at these flowers. It helps. Really!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
