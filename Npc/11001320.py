""" 11001320: Stefan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1216150106000596$
        # - Anyone can enjoy music any time!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1216150106000600$
        # - Anyone can play music if they have an instrument. How would you like to use one created by the Royal Music Academy to begin your musical adventure? 
        if pick == 0:
            # $script:1216150106000601$
            # - I'd love to learn to play music!
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1216150106000602$
        # - If you want to play music, just click an instrument. Isn't that easy? You can improvise or use music scores.
        if pick == 0:
            # $script:1216150106000603$
            # - Music scores? How?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:1216150106000604$
            # - It's easy to use music scores. You can buy preset music scores or buy empty music scores and record music in them. It's a convenient method to play concerts from music you composed. Doesn't that sound like a blast? 
            return 42
        elif self.index == 1:
            # $script:1216150106000605$
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
