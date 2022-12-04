""" 11004127: Veteran Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720130407010497$
        # - Hmph... To think I'd be stationed in a place like this in my twilight years...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720130407010498$
        # - So... tired... When's the next shift change?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
