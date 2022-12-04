""" 11001328: Lakachi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005231$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005234$
        # - Just keep walking. I don't have time for wimps like you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
