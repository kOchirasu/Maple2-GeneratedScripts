""" 11003955: Knight """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010001$
        # - Hi there.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010002$
        # - So you're an adventurer? You seem pretty strong. Nice to meet you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
