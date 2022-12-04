""" 11000254: Jane """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 60

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001056$
        # - How may I help you?
        return None # TODO

    def __60(self, pick: int) -> int:
        # $script:0831180407001060$
        # - Hey, there! If you've got a style in mind, we can make it happen. If you don't, maybe a magazine will inspire you. Want one?
        if pick == 0:
            # $script:0831180407001061$
            # - Yep.
            # TODO: goto 61,62
            # TODO: gotoFail 63
            return 63
        elif pick == 1:
            # $script:0831180407001062$
            # - I'd like some advice.
            return 64
        return -1

    def __61(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407001063$
        # - Sure thing. This has all the latest styles. Have a seat and check them out.
        return -1

    def __62(self, pick: int) -> int:
        # $script:0831180407001064$
        # - Err... I'm afraid you already have the only magazine we have. Sorry about that.
        return -1

    def __63(self, pick: int) -> int:
        # $script:0831180407001065$
        # - Oh, friend... I'm afraid your bag is too heavy. Why don't you lighten it first?
        return -1

    def __64(self, pick: int) -> int:
        # $script:0831180407001066$
        # - Sure! I love nothing more than helping match people with the hair of their dreams. Let's chat and find something that's totally you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (62, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (63, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (64, 0):
            return Option.CLOSE
        return Option.NONE
