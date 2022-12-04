""" 11001098: Moif """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003693$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003696$
        # - Hey, hey! This place is dangerous. Get out of here! We don't need you fouling up any of the valves.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
