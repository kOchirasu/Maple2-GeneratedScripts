""" 11000158: Bruno """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000666$
        # - What seems to be the problem?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000668$
        # - This is bad. The monsters are growing stronger by the day.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000669$
        # - If you're looking for $itemPlural:20000014$, the monsters around here are running around with them.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0116162507009777$
            # - What brings you here, $MyPCName$?
            return 40
        elif self.index == 1:
            # $script:0116162507009778$
            # - Are you really working with $npcName:11003534[gender:0]$? Do you think you could put in a good word?
            if pick == 0:
                # $script:0116162507009779$
                # - Uhh... About what?
                return 41
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:0116162507009780$
        # - Becoming his apprentice! He says that I'm still a rookie, but in just ten years under his tutelage, I could become one of the greatest guards of all time!
        if pick == 0:
            # $script:0116162507009781$
            # - Ten years?!
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:0116162507009782$
        # - Anyway, why are you here?
        if pick == 0:
            # $script:0116162507009783$
            # - I'm looking into rumors about places affected by extreme heat.
            return 43
        return -1

    def __43(self, pick: int) -> int:
        if self.index == 0:
            # $script:0116162507009784$
            # - Extreme heat. I see... 
            return 43
        elif self.index == 1:
            # $script:0116170407009790$
            # - I don't know anything about that!
            return 43
        elif self.index == 2:
            # $script:0116162507009785$
            # - They say $npcName:11000005[gender:1]$ knows just about everything. You could head to $map:02000031$ and ask her.
            if pick == 0:
                # $script:0116162507009786$
                # - Thank you for your time.
                return 44
            return -1
        return -1

    def __44(self, pick: int) -> int:
        # $script:0116162507009787$
        # - It was my pleasure! Please tell $npcName:11003534[gender:0]$ I said hello.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.NEXT
        elif (self.state, self.index) == (43, 1):
            return Option.NEXT
        elif (self.state, self.index) == (43, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (44, 0):
            return Option.CLOSE
        return Option.NONE
