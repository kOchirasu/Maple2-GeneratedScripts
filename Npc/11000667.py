""" 11000667: Lando """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002704$
        # - WHAT?!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002707$
        # - Mm? What? 
        if pick == 0:
            # $script:0831180407002708$
            # - What are you doing?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002709$
            # - You're a curious sort, aren't you? As the old saying goes, ignorance is bliss.
            return 31
        elif self.index == 1:
            # $script:0831180407002710$
            # - Don't stick your nose where it doesn't belong.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
