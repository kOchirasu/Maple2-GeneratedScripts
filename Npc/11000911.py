""" 11000911: Manns """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003275$
        # - I don't want any questions.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003277$
        # - Please don't talk to me. I'm in the middle of doing the worst thing I can imagine.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
