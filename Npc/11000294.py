""" 11000294: Papa Frog """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001171$
        # - May I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407001175$
        # - Croak, croak, croak. Croaaaaakkk...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
