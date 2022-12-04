""" 11004102: NPCNAME_11004102_NAME """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0705145607010425$
        # - SCRIPTNPCNAM_0705145607010425_NAME
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0705145607010427$
            # - SCRIPTNPCNAM_0705145607010427_NAME
            return 30
        elif self.index == 1:
            # $script:0705145607010428$
            # - SCRIPTNPCNAM_0705145607010428_NAME
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
