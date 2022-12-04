""" 11004195: Ereve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010638$
        # - $MyPCName$, what brings you to me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010639$
        # - You must always believe in yourself. Though the road is long and difficult, it is our duty to bring peace to this world.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
