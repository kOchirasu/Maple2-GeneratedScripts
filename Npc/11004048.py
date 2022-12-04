""" 11004048: Carriage Tender """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010069$
        # - It's a long walk to the Frontier Foundation. Why not take a carriage?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010070$
        # - It's a long walk to the Frontier Foundation. Why not take a carriage?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
