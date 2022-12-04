""" 11001601: Jenna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006089$
        # - Do you have business with me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006138$
        # - The real fun is about to begin! I'm going to blow that $npcName:11001231[gender:0]$ guy to smithereens!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
