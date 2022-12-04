""" 11004049: Carriage Tender """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010071$
        # - Would you like a carriage back to Tria?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010072$
        # - Would you like a carriage back to Tria?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
