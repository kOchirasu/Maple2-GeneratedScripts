""" 11001401: Montino """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005401$
        # - Th-this is too high up...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1228164407005741$
        # - I need to climb down sooner or later, but I'm worried that <i>they</i> are still down there.
        if pick == 0:
            # $script:1228164407005742$
            # - Who's they?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1228164407005743$
        # - Those robots! They were supposed to help us develop the desert, but they all went crazy!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
