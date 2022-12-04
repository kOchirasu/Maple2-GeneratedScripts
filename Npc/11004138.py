""" 11004138: Doctor Harold """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0730132107010541$
        # - Sigh, another patient?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0730132107010542$
        # - And just who's going to treat <i>my</i> injuries?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
