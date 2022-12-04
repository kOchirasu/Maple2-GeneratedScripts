""" 11001931: Apprentice Ladme """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1122150407007454$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1122214707007472$
        # - I can't afford these materials. I'll just have to get some on my own... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
