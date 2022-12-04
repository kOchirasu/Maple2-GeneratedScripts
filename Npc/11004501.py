""" 11004501: Drill Sergeant """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012407$
        # - You here to enlist? Fall in line, Recruit!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012408$
        # - You here to enlist? Fall in line, Recruit!
        if pick == 0:
            # $script:1227192907012409$
            # - I'm not your recruit.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012410$
            # - Is that so? Hmph. You have the look of a washed-up loser. Join my troop and I'll have you back on your feet in no time!
            return 11
        elif self.index == 1:
            # $script:1227192907012411$
            # - We need all the help we can get to fight Tairen. We'll even take folks wearing... whatever that's supposed to be. You sure you don't want to sign on with us?
            if pick == 0:
                # $script:1227192907012412$
                # - I'll think about it...
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:1227192907012413$
        # - Whenever and wherever, we're ready!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
