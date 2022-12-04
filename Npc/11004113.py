""" 11004113: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010469$
        # - I am ready to leave at a moments notice.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010470$
        # - Guidance has been retasked toward the recovery of Lapenshards.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
