""" 11001012: Langley """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003454$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003457$
        # - I'm sure you heard that time stopped here in Ludibrium. Now I don't have to worry about getting old, as long as I stay here.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
