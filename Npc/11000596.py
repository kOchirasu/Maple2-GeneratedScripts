""" 11000596: Ting """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002392$
        # - I'm busy, so busy!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002395$
        # - I have to do homework, and I have to study... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
