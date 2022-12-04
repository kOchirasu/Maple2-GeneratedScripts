""" 11003536: Nairin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1126150707011935$
        # - Would you like to take on a mission for Green Hoods?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1126150707011936$
        # - How may I help you today, $male:Sir,female:Ma'am$?
        if pick == 0:
            # $script:1126150707011937$
            # - Why are Green Hoods here?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:1126150707011938$
            # - That's a good question! Most people think we're simple rangers and woodswomen, wandering the forests of Henesys with our bows.
            return 31
        elif self.index == 1:
            # $script:1126150707011939$
            # - But we're so much more than that! We know all about helping people and making sure they have everything they need.
            return 31
        elif self.index == 2:
            # $script:1126150707011940$
            # - There's more to keeping the peace than simply being a good fighter. You need to know how to treat a wound and provide a shoulder to cry on.
            return 31
        elif self.index == 3:
            # $script:1126150707011941$
            # - That's why we've been entrusted with support operations on Sky Fortress.
            return 31
        elif self.index == 4:
            # $script:1126150707011942$
            # - Of course, you know firsthand how good we are in a fight. Even though I'm stationed up here on the bridge, I'm just as good with my bow as Eka!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.NEXT
        elif (self.state, self.index) == (31, 3):
            return Option.NEXT
        elif (self.state, self.index) == (31, 4):
            return Option.CLOSE
        return Option.NONE
