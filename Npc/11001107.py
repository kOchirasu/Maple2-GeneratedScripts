""" 11001107: Vena """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003719$
        # - Mm... T-that's... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003722$
        # - Mom was right. She said anything can come true if I pray hard enough. I've prayed every day to be able to go back to her. Now I can!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
