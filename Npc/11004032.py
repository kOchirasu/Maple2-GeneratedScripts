""" 11004032: Lanemone """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010049$
        # - What is it, kid? You want to know about lapenshards?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010050$
        # - What is it, kid? You want to know about lapenshards?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
