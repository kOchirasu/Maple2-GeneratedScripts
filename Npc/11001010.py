""" 11001010: Thurman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003446$
        # - What do I do now?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003449$
        # - Do you think the pirates will pay their tab if I ask nicely?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
