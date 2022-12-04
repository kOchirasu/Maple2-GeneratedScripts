""" 11004035: Orde """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010055$
        # - It's not like I want to be here. But I've got a debt to repay.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010056$
        # - It's not like I want to be here. But I've got a debt to repay.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
