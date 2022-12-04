""" 11003161: Troy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008067$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0306155707008069$
        # - If you love flowers so much, then go pick them yourself. These aren't for you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
