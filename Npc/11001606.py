""" 11001606: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006094$
        # - You're here.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006143$
        # - Has the time finally come time to avenge Arazaad? $npcName:11001231[gender:0]$... I'll make you pay!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
