""" 11000258: Hoon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001067$
        # - What seems to be the problem?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001068$
        # - Please keep your voice down. I'm not supposed to be talking with anyone right now.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
