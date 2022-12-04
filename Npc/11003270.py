""" 11003270: Jin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008222$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008223$
        # - If only Captain Stilton were still alive... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
