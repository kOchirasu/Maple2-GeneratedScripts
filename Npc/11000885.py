""" 11000885: Rabiette """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003245$
        # - Where am I right now? Sniff, sniff...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003248$
        # - Sniff... Human, have you been to the moon? There are no stars or moon here...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
