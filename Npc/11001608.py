""" 11001608: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006096$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006145$
        # - I hope everyone's all right. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
