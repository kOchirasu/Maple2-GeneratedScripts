""" 11001342: Venchas """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005288$
        # - Sigh... This is getting tiring...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005291$
        # - You can't swat a bug in the water, but you can still spray it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
