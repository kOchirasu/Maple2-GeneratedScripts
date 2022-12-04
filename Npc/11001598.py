""" 11001598: Rolling Thunder """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006086$
        # - Hey, welcome!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006135$
        # - What's-his-name, $npcName:11001231[gender:0]$? C'mon, let's get him! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
