""" 11000181: Gilbert """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000750$
        # - What?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000754$
        # - I've been working at this junkyard for over a decade, and this must be the strangest thing that has ever happened.
        if pick == 0:
            # $script:0831180407000755$
            # - What is it?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000756$
            # - A while back, a carriage full of junk came in with some Royal Guard weapons. I figured it must have been a mistake, so I checked with $npcName:11000171[gender:0]$. He said they were to be melted down, now that the court was canceled.
            return 41
        elif self.index == 1:
            # $script:0831180407000757$
            # - If that were the case, the palace should've sent them to the forge instead of a junkyard. Right?
            if pick == 0:
                # $script:0831180407000758$
                # - Yeah.
                return 42
            elif pick == 1:
                # $script:0831180407000759$
                # - Nah.
                return 43
            return -1
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407000760$
        # - Right on. And I even saw $npcName:11000171[gender:0]$ sell the iron from the palace weapons to some dealer. How crazy do you have to be to steal from the palace? 
        return -1

    def __43(self, pick: int) -> int:
        # $script:0831180407000761$
        # - Really? Huh. Maybe it's just me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        return Option.NONE
