""" 11001305: Manovich """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005024$
        # - $MyPCName$, what is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228222807005746$
        # - No wonder the empress was in such a hurry to see me. It's always something... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
