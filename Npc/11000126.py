""" 11000126: Poffo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000545$
        # - Um... Hi. What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000548$
        # - I mustered up the courage to come here, but now I'm too scared to move. I have to hunt monsters, or get the treasure from the cliff. I need the money...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
