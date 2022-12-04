""" 11001576: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006064$
        # - Don't worry too much. 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006118$
        # - I think everyone... will be all right... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
