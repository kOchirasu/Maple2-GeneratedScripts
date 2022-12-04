""" 11001139: Lavoy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911192907003897$
        # - I'm selling these fine leather jackets.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0911192907003900$
        # - Hey, I've seen you hunting monsters around here before, haven't I?
        if pick == 0:
            # $script:0911192907003901$
            # - Yep!
            return 31
        elif pick == 1:
            # $script:0911192907003902$
            # - Nope!
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0911192907003903$
        # - Haha! I could tell just by looking at you! A great adventurer, surely in need of Lavoy's fine leather goods!
        if pick == 0:
            # $script:0911192907003904$
            # - I'm not interested.
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # $script:0911192907003905$
        # - Don't be silly, I know a famous adventurer when I see one! A great adventurer deserves a great outfit. How many leather jackets can I put you down for?
        if pick == 0:
            # $script:0911192907003906$
            # - Sorry, not interested.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0911192907003907$
        # - Hahaha! You say that now, but you'll find no finer leatherwork around. Return to me once you've changed your mind.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
