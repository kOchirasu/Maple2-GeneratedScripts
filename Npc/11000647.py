""" 11000647: Prisoner 160920 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002646$
        # - Get me out of here... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002650$
        # - What are you lookin' at? This ain't no zoo, and I ain't no animal! Ahhh, I hate alla you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
