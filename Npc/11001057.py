""" 11001057: Stark """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003608$
        # - Oh, no... 
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003611$
            # - I look older than $npcName:11001028[gender:0]$. Well, thanks, I guess.
            return 30
        elif self.index == 1:
            # $script:0831180407003612$
            # - $npcName:11001028[gender:0]$ looks young because he's bald, but he's the same age I am. Maybe I should shave my head, too. 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
