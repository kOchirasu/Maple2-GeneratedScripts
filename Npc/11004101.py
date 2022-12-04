""" 11004101: NPCNAME_11004101_NAME """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0705145607010421$
        # - SCRIPTNPCNAM_0705145607010421_NAME
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0705145607010423$
        # - SCRIPTNPCNAM_0705145607010423_NAME
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
