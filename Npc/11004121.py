""" 11004121: Green Hood """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010485$
        # - I'll let you know if I detect any unusual movement inside the blast radius.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010486$
        # - See something, say something!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
