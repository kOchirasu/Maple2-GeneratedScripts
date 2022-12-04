""" 11004054: Rejan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010081$
        # - My master and the leaders of Terrun Calibre will definitely return. Until then, I'll carry out their will.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010082$
        # - My master and the leaders of Terrun Calibre will definitely return. Until then, I'll carry out their will.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
