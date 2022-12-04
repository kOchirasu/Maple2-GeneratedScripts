""" 11003203: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0518141907008520$
        # - Training to be a guard is tough.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0518141907008521$
        # - Huh...? Who is this small friend?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
