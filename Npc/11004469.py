""" 11004469: Indica """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012119$
        # - That little cretin wants to go out and play...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012120$
        # - That little cretin wants to go out and play...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
