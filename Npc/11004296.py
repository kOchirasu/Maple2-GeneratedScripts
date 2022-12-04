""" 11004296: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011366$
        # - How lovely!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1002141907011369$
        # - Tell me, what's the one thing you must never, ever forget when you travel?
        if pick == 0:
            # $script:1002141907011370$
            # - Your wallet, of course.
            return 31
        elif pick == 1:
            # $script:1002141907011371$
            # - You can't travel without a suitcase.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011372$
        # - Oh! I suppose your wallet <i>is</i> important. But is it the most important? Think harder!
        if pick == 0:
            # $script:1002141907011373$
            # - You can't travel without a suitcase.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1002141907011374$
        # - That's right! All of your most important things go in your suitcase, after all. If you're looking for something, you should always check your suitcase first.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
