""" 11004158: Miel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010587$
        # - It's so close, but I can't reach it. It comes to me in the night and vanishes at dawn.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010588$
        # - Many things shine, not all of them valuable.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
