""" 11000890: Ringling """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003254$
        # - What is it? What is it? What is it? There has to be a reason...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003256$
        # - What brings you here?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
