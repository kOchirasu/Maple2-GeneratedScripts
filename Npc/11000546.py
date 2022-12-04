""" 11000546: Ebby """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002318$
        # - What seems to be the problem?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002319$
        # - Want to see what I've got inside this bundle? Then show me your wallet first! Ha, just kidding...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
