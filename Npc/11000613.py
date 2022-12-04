""" 11000613: Louie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002508$
        # - Huh?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002510$
        # - No one knows what it's like to toil in this place. Only another captive could understand. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
