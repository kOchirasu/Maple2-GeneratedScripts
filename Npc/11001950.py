""" 11001950: Mareda """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123165007007496$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1208184307007548$
        # - First, I'll learn how to play the harp. Then I'll let my hair down, and wear a flowing white gown, and spend all day plucking on the strings. I'll look so pretty!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
