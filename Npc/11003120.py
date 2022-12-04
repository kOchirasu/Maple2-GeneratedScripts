""" 11003120: Wei Hong """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0321141707008118$
        # - I don't have time for small potatoes.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0321141707008121$
        # - I don't know you, so I'll warn you once: Don't cross me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
