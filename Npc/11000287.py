""" 11000287: Bag """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001127$
        # - Check the altar.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001128$
        # - This altar is covered in layers of dust, the result of ages of neglect.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
