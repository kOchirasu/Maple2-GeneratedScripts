""" 11003267: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008214$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008217$
        # - I am captain of the Royal Guard. Each and every one of my men would lay down his life in service to Empress $npcName:11000075[gender:1]$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
