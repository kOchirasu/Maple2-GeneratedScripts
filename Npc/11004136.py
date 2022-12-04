""" 11004136: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0730132107010537$
        # - Your aura is one of virtue.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0730132107010538$
        # - All that lifeforce... will you give it to me?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
