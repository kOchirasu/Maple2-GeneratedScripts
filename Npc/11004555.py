""" 11004555: Tristan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0123111007012734$
        # - Anything might happen now...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0123111007012735$
        # - Anything might happen now...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
