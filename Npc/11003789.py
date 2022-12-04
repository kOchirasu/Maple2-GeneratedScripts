""" 11003789: Tristan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1213192607009648$
        # - Let's get to business.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1213192607009649$
        # - ...Finally, the time has come.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
