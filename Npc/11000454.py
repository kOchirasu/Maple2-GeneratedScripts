""" 11000454: Teo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002006$
        # - I'm a seasoned sailor!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002009$
        # - Ahoy there! Have you ever seen a whale?
        if pick == 0:
            # $script:0831180407002010$
            # - Yes.
            return 31
        elif pick == 1:
            # $script:0831180407002011$
            # - Nope.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407002012$
        # - Bah, nonsense! I've been a fisherman my whole life, and only seen a whale once. And it was a teeny one at that! Me dream is to see the great blue whale just once before the sea takes me.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407002013$
        # - Aye, they're an elusive catch. I've always wanted to see a blue whale myself.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
