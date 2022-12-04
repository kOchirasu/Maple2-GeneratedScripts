""" 11000958: Ruman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003319$
        # - Aww, my poor scaredy-cats!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003321$
        # - My babies are as precious as children to me. Hee hee.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
