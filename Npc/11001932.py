""" 11001932: Apprentice Tochi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1122150407007455$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1122214707007475$
        # - Handicrafts are so fun that I often lose track of the time. I just wish I had someone to actually give this stuff to... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
