""" 11001011: Navue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003450$
        # - Well, there goes the neighborhood.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003453$
        # - My realtor said that I'd only hear the sound of waves. I wouldn't have come here if I knew my neighbors would be so terrible.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
