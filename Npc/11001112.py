""" 11001112: Bella's Soul """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003738$
        # - Do you know me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003739$
        # - I... I can't go back like this... No... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
