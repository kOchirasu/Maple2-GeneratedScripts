""" 11004559: Mint """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014487$
        # - Aaaah.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014488$
            # - Aaaah.
            return 10
        elif self.index == 1:
            # $script:0220211107014489$
            # - Oh, hello! I remember you.
            if pick == 0:
                # $script:0220211107014490$
                # - Yeah, and I've seen you around.
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014491$
            # - I suppose it would be weird if you <i>didn't</i> know who I am.
            return 20
        elif self.index == 1:
            # $script:0220211107014492$
            # - So, you're here for the Queen Bean Rumble, right? Are you sure you're up to fighting me?
            if pick == 0:
                # $script:0220211107014493$
                # - I was about to ask you the same.
                return 30
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0220211107014494$
        # - Oh, you think you can take me on just because I dance all day? Well, I have news for you, $male:buddy,female:lady$. Dancing is fantastic exercise. I'm going to crush you like a teeny tiny bug!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
