""" 11004062: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010097$
        # - Just let us know if there's anything we can do to help.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010098$
        # - Just let us know if there's anything we can do to help.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
