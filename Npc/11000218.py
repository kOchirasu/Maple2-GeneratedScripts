""" 11000218: Billy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000951$
        # - What is it?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000955$
        # - People should be good to each other. You reap what you sow, as they say...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
