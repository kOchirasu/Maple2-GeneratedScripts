""" 11000385: Shalin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001568$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001570$
        # - If you see trash on the street, by all means pick it up! Everyone has to do their part to keep their homes clean.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
