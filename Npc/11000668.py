""" 11000668: Niro """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002711$
        # - WHAT?!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002714$
        # - Wait, are you going to go down to the basement?
        if pick == 0:
            # $script:0831180407002715$
            # - Yep!
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002716$
            # - Ha! You're funny. I don't know how you got down here, but trust me when I say you NEVER want to go to the 2nd basement. There are some really scary guys down there.
            return 31
        elif self.index == 1:
            # $script:0831180407002717$
            # - It's just as well, I don't feel like dealing with you myself. Go on, go to the basement. And don't say I didn't warn you. 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
