""" 11001959: Fallen Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1201224107007508$
        # - Ugh...  
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1201224107007510$
        # - They took $npcName:11000526[gender:0]$...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
