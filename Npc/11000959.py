""" 11000959: Darren """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003322$
        # - Step back. You stand around gawking like that and you're sure to get eaten.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003324$
        # - It's hard enough to keep black market dealers from slipping in from $map:02000100$. Now we have to deal with these stupid monsters!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
