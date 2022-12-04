""" 11001943: Gichak """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123165007007489$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1208184307007527$
        # - Lazy designers! These are the exact same clothes they had here yesterday. Where are the new designs?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
