""" 11004159: Beatrice """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0730132107010543$
        # - I pray everyone is safe...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0730132107010544$
        # - Please don't overexert yourself.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
