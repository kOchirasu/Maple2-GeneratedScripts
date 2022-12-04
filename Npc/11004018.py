""" 11004018: Surnuny """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010023$
        # - Hey! I've seen you around Tria!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010024$
        # - I'm Surnuny, Tria's best weapons merchant. I came here to trade.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
