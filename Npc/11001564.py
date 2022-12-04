""" 11001564: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006052$
        # - There you are.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006108$
        # - No matter $npcName:11001231[gender:0]$'s reasons or excuses, I will never forgive him for murdering Arazaad.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
