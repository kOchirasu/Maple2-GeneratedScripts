""" 11000264: Ladin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001077$
        # - Need something?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001080$
        # - After the Blue Lapenta broke, top scholars from across the world descended on the $map:02000026$. Ultimately, I am confident that it will be an alchemist to uncover the secrets of the Land of Darkness and the Shadow World.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407001081$
        # - Can't you see I'm trying to focus?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
