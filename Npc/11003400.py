""" 11003400: Rovey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0621181107008568$
        # - Focus on your training.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0621181107008569$
        # - Willpower alone does not make you a knight.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
