""" 11004019: Surnuny """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010025$
        # - Something's wrong... My fur's standing on end.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010026$
        # - Something's wrong... My fur's standing on end.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
