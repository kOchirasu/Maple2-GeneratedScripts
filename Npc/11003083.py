""" 11003083: Celine """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0113143107007770$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0113143107007771$
        # - $MyPCName$, I'm sorry you came all the way here for nothing.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
