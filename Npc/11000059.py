""" 11000059: Oyako """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000261$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000264$
        # - Do you live here?
        if pick == 0:
            # $script:0831180407000265$
            # - Yep!
            return 31
        elif pick == 1:
            # $script:0831180407000266$
            # - Nope!
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000267$
        # - I knew it! I can tell you're from the city by your looks. How much money do you have to make to live in a neighborhood like this?
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000268$
        # - Oh, no. You look so pale, I-I thought you lived here. I've never been to such a big place before, and everything is so amazing here. And I think I've seen more people today than I've ever seen in my hometown.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
