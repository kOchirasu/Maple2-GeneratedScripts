""" 11001458: Fin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1222171407005462$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1222171407005465$
        # - We aren't some fly-by-night operation. We're the Blackstars!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
