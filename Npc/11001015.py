""" 11001015: Yena """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003459$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003462$
        # - Each magic-user has their own spell. I haven't chosen mine yet. Alio olio! Hoi, hoi! Chacharachat! Which one sounds the best to you?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
