""" 11001055: Sansakova """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003606$
        # - Welcome.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003607$
        # - No pizza can match Maggiore pizza. Chewy dough with simple toppings, just like Mom used to make! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
