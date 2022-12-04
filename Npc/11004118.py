""" 11004118: Royal Watchman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010479$
        # - If I see anything unusual, I'll report in right away!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010480$
        # - The blast area was pretty big...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
