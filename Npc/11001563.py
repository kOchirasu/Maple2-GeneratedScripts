""" 11001563: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006051$
        # - You're here.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0515180307006106$
            # - $MyPCName$, $npcName:11001232[gender:1]$ says she misses you. 
            return 10
        elif self.index == 1:
            # $script:0515180307006107$
            # - I'm sorry I didn't stay in touch. I couldn't find the time. Still, it seems you did well enough without me.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
