""" 11001520: Swordsman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515211707006107$
        # - Nice to meet you!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515211707006108$
        # - I'm honored to join the Starlight Expedition. The captain of the guard sent me to help $npc:11000076[gender:0]$. I intend to win glory for the guard!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
