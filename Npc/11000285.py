""" 11000285: Torhara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001114$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001117$
        # - Is there someone you love?
        if pick == 0:
            # $script:0831180407001118$
            # - Yes.
            return 31
        elif pick == 1:
            # $script:0831180407001119$
            # - No.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407001120$
        # - Good for you. Cherish them while you can. Have you ever lost someone you love?
        if pick == 0:
            # $script:0831180407001121$
            # - Yes.
            return 33
        elif pick == 1:
            # $script:0831180407001122$
            # - No.
            return 34
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407001123$
        # - I see. Sometimes love begets tragedy, but it's worth more than the pain. 
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407001124$
        # - I see. I daresay I understand your pain. 
        return -1

    def __34(self, pick: int) -> int:
        # $script:0831180407001125$
        # - I see. Let me give you some advice. Never take the ones you love for granted. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
