""" 11004479: Meryl """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012196$
        # - Oh! You startled me.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012197$
            # - Oh! You startled me.
            return 10
        elif self.index == 1:
            # $script:1227192907012198$
            # - I'm here to study aetherine. We're really just scratching the surface when it comes to possible applications!
            if pick == 0:
                # $script:1227192907012199$
                # - What have you learned so far?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012200$
            # - Well, aetherine can make objects spontaneously levitate for almost no energy expenditure. I've measured the amount of aetherine in the floating buildings here, and there's very, very little.
            return 11
        elif self.index == 1:
            # $script:1227192907012201$
            # - Our own levitation technology requires massive amounts of energy to work. If we can switch to aetherine, it will be a technological revolution!
            return 11
        elif self.index == 2:
            # $script:1227192907012202$
            # - Of course, I don't know how any of it works. But I will. Oh yes, I will...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.CLOSE
        return Option.NONE
