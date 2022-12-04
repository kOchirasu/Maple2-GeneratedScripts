""" 11001302: Ereve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005020$
        # - $MyPCName$, what brings you to me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1215203907005021$
        # - $MyPCName$, please don't disappoint me. I know it's difficult, but keep up your efforts to save our world.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
