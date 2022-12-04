""" 11001040: Fordson """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003552$
        # - The wind is so cold.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003555$
        # - Maritime Leaguers are atmospheric, oceanic, and geologic specialists gathered to observe and collect information about the oceans and everything in it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
