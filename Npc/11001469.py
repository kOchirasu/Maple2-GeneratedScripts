""" 11001469: Arl """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1223040807005536$
        # - This must be the place.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1223040807005539$
        # - Shhh! Don't tell my mom I'm here!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
