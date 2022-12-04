""" 11004029: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010045$
        # - Do you have something to tell me?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010046$
        # - Do you have something to tell me?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
