""" 11200002: Antonius """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1214161306000880$
        # - Anyone can enjoy music any time!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1214161306000884$
        # - Anyone can play music if they have an instrument. How would you like to use one created by the Royal Music Academy to begin your musical adventure? 
        if pick == 0:
            # $script:1214161306000885$
            # - I'd love to learn to play music!
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1214161306000886$
        # - If you want to play music, just click an instrument. Isn't that easy? You can improvise or use music scores.
        if pick == 0:
            # $script:1214161306000887$
            # - Music scores? How?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:1214161306000888$
            # - It's easy to use music scores. You can buy preset music scores or buy empty music scores and record music in them. It's a convenient method to play concerts from music you composed. Doesn't that sound like a blast? 
            return 42
        elif self.index == 1:
            # $script:1214161306000889$
            # - No matter where you are, music is there! Take a look at the items I have for you, and give music a try!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.CLOSE
        return Option.NONE
