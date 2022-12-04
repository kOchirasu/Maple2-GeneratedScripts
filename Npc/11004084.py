""" 11004084: Torchy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0622133907010284$
        # - Shh! You'll wake up the other fireflies. No loud noises allowed.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010285$
            # - Shh! You'll wake up the other fireflies. No loud noises allowed.
            return 10
        elif self.index == 1:
            # $script:0622133907010286$
            # - Quietly, now... You're here looking for a quiet place to rest, aren't you?
            if pick == 0:
                # $script:0622133907010287$
                # - What makes you think that?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010288$
            # - Humans always come here when something's on their mind. Our pretty light helps them feel better! I figured you might be the same.
            return 31
        elif self.index == 1:
            # $script:0622133907010289$
            # - I can't do a danged thing to actually help you. But hey, if staring at our sparkly heinies brings you peace, then stare away!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
