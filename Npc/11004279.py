""" 11004279: Nazkar Statue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011287$
        # - <font color="#909090">(This is a statue of the guardian deity of Nazkar.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011288$
            # - <font color="#909090">(This is a statue of the guardian deity of Nazkar.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011289$
            # - <font color="#909090">(The $map:02010034$ was the holiest sanctum of the lumarigons, the great dragons of light. Only the worthiest of the worthy could set foot in these halls.)</font>
            return 10
        elif self.index == 2:
            # $script:0911203207011290$
            # - <font color="#909090">(In spite of the spreading darkness, there's still a glimmer of the light in this statue's eyes...)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
