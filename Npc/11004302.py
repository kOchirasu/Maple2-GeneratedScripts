""" 11004302: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011418$
        # - I'mma scratch <i>everything!</i>
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1002141907011422$
            # - Now I'mma ghost, I can talk to people! How fun!
            return 30
        elif self.index == 1:
            # $script:1002141907011423$
            # - 'Cause I'm inna good mood, I'mma tell you a secret! Watch the floors around here, or you're gonna fall!
            if pick == 0:
                # $script:1002141907011424$
                # - What's that supposed to mean?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011425$
        # - Your foot's gonna fall! Watch the floors! Got it?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
