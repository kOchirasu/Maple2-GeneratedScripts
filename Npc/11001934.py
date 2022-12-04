""" 11001934: Apprentice Monis """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1122150407007457$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1122214707007481$
        # - Sorry, but I'm not in the mood to chat. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
